import os
from dotenv import load_dotenv
from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError

# Cargar variables desde .env
load_dotenv()

def call_sap_rfc(rfc_name: str, parameters: dict):
    conn = Connection(
        user=os.getenv("SAP_USER"),
        passwd=os.getenv("SAP_PASS"),
        ashost=os.getenv("SAP_ASHOST"),
        sysnr=os.getenv("SAP_SYSNR"),
        client=os.getenv("SAP_CLIENT"),
        lang=os.getenv("SAP_LANG", "ES")
    )
    return conn.call(rfc_name, **parameters)

# ✅ NUEVA FUNCIÓN DE PRUEBA DE CONEXIÓN
def check_sap_connection():
    try:
        conn = Connection(
            user=os.getenv("SAP_USER"),
            passwd=os.getenv("SAP_PASS"),
            ashost=os.getenv("SAP_ASHOST"),
            sysnr=os.getenv("SAP_SYSNR"),
            client=os.getenv("SAP_CLIENT"),
            lang=os.getenv("SAP_LANG", "ES")
        )
        conn.close()
        return {"status": "ok"}
    except (CommunicationError, LogonError, ABAPRuntimeError, ABAPApplicationError) as e:
        return {"status": "error", "message": str(e)}
