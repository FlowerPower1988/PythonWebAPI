from fastapi import APIRouter, Depends, HTTPException
from app.abstraction.repositories.order_product_manager_interface import IOrder_productManager
from container import get_order_product_manager
from ..model.order_product import  Order_product, Order_productValues

router4 = APIRouter()

@router4.get("/orders_products/", response_model=list[Order_product])
def read_orders_products(order_product_manager: IOrder_productManager = Depends(get_order_product_manager)):
    return order_product_manager.read_orders_products()

@router4.post("/order_products/", response_model=Order_product)
def create_order_product(order_product: Order_productValues, order_product_manager: IOrder_productManager = Depends(get_order_product_manager)): 
    return order_product_manager.create_order_product(order_product)

@router4.get("/order_products/{order_id}", response_model=list[Order_product])
def read_order_product(order_id: int, order_product_manager: IOrder_productManager = Depends(get_order_product_manager)):
    
    order_product = order_product_manager.read_order_product(order_id)
    
    if not order_product:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    
    return order_product

@router4.put("/order/{order_id}/product/{product_id}", response_model=Order_product)
def update_order_product(order_id: int, product_id: int, amount: int, order_product_manager: IOrder_productManager = Depends(get_order_product_manager)):
    order_product = order_product_manager.update_order_product(order_id, product_id, amount)
    
    if not order_product:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} with product {product_id} not found")
    
    return order_product

@router4.delete("/order/{order_id}/product/{product_id}", response_model=None)
def delete_order_product(order_id: int, product_id: int, order_product_manager: IOrder_productManager = Depends(get_order_product_manager)):
    id_exist = order_product_manager.delete_order_product(order_id, product_id)
    if not id_exist:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} with product {product_id} not found")
    
    return id_exist