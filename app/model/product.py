from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints
from app.model.db_base import DBBase

Str1To20Chars = Annotated[
    str,
    StringConstraints(
        min_length=1,
        max_length=20,
    )
]

PositiveFloat = Annotated[
    float, 
    Field(
        strict=True, 
        gt=0
    )
]

class ProductValues(BaseModel):
    name: Str1To20Chars
    price: PositiveFloat

class Product(ProductValues,DBBase,BaseModel):
    pass
    
    
    



