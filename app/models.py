from pydantic import BaseModel
from typing import Dict

class RFCRequest(BaseModel):
    rfc_name: str
    parameters: Dict
