from pydantic import BaseModel
from abc import ABC

class DBBase(ABC, BaseModel):
    id: int
