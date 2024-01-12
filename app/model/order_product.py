from typing import Annotated
from pydantic import BaseModel, Field
from app.model.db_base import DBBase

class Order_productValues(BaseModel):
    order_id: int
    product_id: int
    amount: int
    
class Order_product(Order_productValues,BaseModel):
    pass
