from fastapi import APIRouter, Depends, HTTPException
from app.abstraction.repositories.order_manager_interface import IOrderManager
from container import get_order_manager
from ..model.order import  Order, OrderValues

router3 = APIRouter()

@router3.post("/orders/", response_model=Order)
def create_order(order: OrderValues, order_manager: IOrderManager = Depends(get_order_manager)): 
    return order_manager.create_order(order)

@router3.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int, order_manager: IOrderManager = Depends(get_order_manager)):
    
    order = order_manager.read_order(order_id)
    
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    
    return order

@router3.get("/orders/", response_model=list[Order])
def read_orders(order_manager: IOrderManager = Depends(get_order_manager)):
    return order_manager.read_orders()

@router3.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order_values: OrderValues, order_manager: IOrderManager = Depends(get_order_manager)):
    order = order_manager.update_order(order_id, order_values)
    
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    
    return order

@router3.delete("/orders/{order_id}", response_model=None)
def delete_order(order_id: int, order_manager: IOrderManager = Depends(get_order_manager)):
    id_exist = order_manager.delete_order(order_id)
    if not id_exist:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    elif id_exist==409:
        raise HTTPException(status_code=409, detail=f"Order with ID {order_id} has ordered products")
    return id_exist