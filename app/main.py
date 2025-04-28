from fastapi import FastAPI
from app.models import RFCRequest
from app.rfc import call_sap_rfc, check_sap_connection

app = FastAPI()

@app.post("/call-rfc")
def call_rfc(request: RFCRequest):
    try:
        result = call_sap_rfc(request.rfc_name, request.parameters)
        return {"status": "ok", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.get("/health")
def health_check():
    return check_sap_connection()
