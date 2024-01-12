from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints
from app.model.db_base import DBBase

Str1To20Chars = Annotated[
    str,
    StringConstraints(
        min_length=1,
        max_length=20,
    )
] 

class UserValues(BaseModel):
    name: Str1To20Chars
    email: EmailStr

class User(UserValues,DBBase,BaseModel):
    pass
    
    
    



