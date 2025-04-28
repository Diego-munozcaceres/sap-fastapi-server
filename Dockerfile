FROM python:3.9-slim

# Instalar herramientas necesarias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libssl-dev \
    libffi-dev \
    cmake \
    git \
    build-essential \
    curl \
    && apt-get clean

# Copiar SDK de SAP al contenedor
COPY sdk/nwrfcsdk /nwrfcsdk

ENV SAPNWRFC_HOME=/nwrfcsdk

# Configurar variables de entorno para el compilador
ENV NWRFCSDK_INCLUDE_DIR=/nwrfcsdk/include
ENV NWRFCSDK_LIB_DIR=/nwrfcsdk/lib
ENV LD_LIBRARY_PATH=/nwrfcsdk/lib

# Establecer carpeta de trabajo
WORKDIR /app

# Copiar requirements y código de la app
COPY requirements.txt .
COPY app ./app

# Instalar dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Clonar y compilar PyRFC desde el repo oficial
RUN git clone https://github.com/SAP/PyRFC.git && \
    ls -la PyRFC && \
    pip install ./PyRFC

# Puerto expuesto
EXPOSE 8080

# Comando para iniciar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

