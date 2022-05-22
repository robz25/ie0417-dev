"""
Basic REST API server example using FastAPI.
"""

from typing import Optional, List
from pydantic import BaseModel

class Device(BaseModel):
    identifier: str
    tipo: str           # type is a reserved word 
    commands : List[str]
    IP : str

class Commands(BaseModel):
    device_identifier: str 
    command: str
    arguments : Optional[List[str]] = None 