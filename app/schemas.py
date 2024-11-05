# app/schemas.py
from pydantic import BaseModel

class EvaluateRequest(BaseModel):
    object_path: str
    competition_id: str
