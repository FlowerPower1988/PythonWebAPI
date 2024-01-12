from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints
from app.model.db_base import DBBase
from datetime import date

Str1To20Chars = Annotated[
    str,
    StringConstraints(
        min_length=1,
        max_length=20,
    )
]

Str6To10Chars = Annotated[
    str,
    StringConstraints(
        min_length=6,
        max_length=10,
    )
]

PositiveFloat = Annotated[
    float, 
    Field(
        strict=True, 
        gt=0
    )
]



class OrderValues(BaseModel):
    user_id: int
    street_name: Str1To20Chars
    postal_code: Str6To10Chars #country?? long of postal code depends on the country
    city: Str1To20Chars 
    date_of_order: date
    total_price: PositiveFloat
    tax: PositiveFloat
    
class Order(OrderValues,DBBase,BaseModel):
    pass
    
    
    



