from fastapi import APIRouter, Depends, HTTPException
from app.abstraction.repositories.user_manager_interface import IUserManager
from container import get_user_manager
from ..model.user import  User, UserValues

from app.abstraction.repositories.product_manager_interface import IProductManager
from container import get_product_manager
from ..model.product import  Product, ProductValues

from app.abstraction.repositories.order_manager_interface import IOrderManager
from container import get_order_manager
from ..model.order import  Order, OrderValues

router = APIRouter()

#-----USER
@router.post("/users/", response_model=User)
def create_user(user: UserValues, user_manager: IUserManager = Depends(get_user_manager)): 
    return user_manager.create_user(user)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, user_manager: IUserManager = Depends(get_user_manager)):
    
    user = user_manager.read_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    return user

@router.get("/users/", response_model=list[User])
def read_users(user_manager: IUserManager = Depends(get_user_manager)):
    return user_manager.read_users()

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_values: UserValues, user_manager: IUserManager = Depends(get_user_manager)):
    user = user_manager.update_user(user_id, user_values)
    
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    return user

@router.delete("/users/{user_id}", response_model=None)
def delete_user(user_id: int, user_manager: IUserManager = Depends(get_user_manager)):
    id_exist = user_manager.delete_user(user_id)
    if not id_exist:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    return id_exist

#-----PRODUCT
@router.post("/products/", response_model=Product)
def create_product(product: ProductValues, product_manager: IProductManager = Depends(get_product_manager)): 
    return product_manager.create_product(product)

@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, product_manager: IProductManager = Depends(get_product_manager)):
    
    product = product_manager.read_product(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    
    return product

@router.get("/products/", response_model=list[Product])
def read_products(product_manager: IProductManager = Depends(get_product_manager)):
    return product_manager.read_products()

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_values: ProductValues, product_manager: IProductManager = Depends(get_product_manager)):
    product = product_manager.update_product(product_id, product_values)
    
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    
    return product

@router.delete("/products/{product_id}", response_model=None)
def delete_product(product_id: int, product_manager: IProductManager = Depends(get_product_manager)):
    id_exist = product_manager.delete_product(product_id)
    if not id_exist:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    
    return id_exist


#-----ORDER
@router.post("/orders/", response_model=Order)
def create_order(order: OrderValues, order_manager: IOrderManager = Depends(get_order_manager)): 
    return order_manager.create_order(order)

@router.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int, order_manager: IOrderManager = Depends(get_order_manager)):
    
    order = order_manager.read_order(order_id)
    
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    
    return order

@router.get("/orders/", response_model=list[Order])
def read_orders(order_manager: IOrderManager = Depends(get_order_manager)):
    return order_manager.read_orders()

@router.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order_values: OrderValues, order_manager: IOrderManager = Depends(get_order_manager)):
    order = order_manager.update_order(order_id, order_values)
    
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    
    return order

@router.delete("/orders/{order_id}", response_model=None)
def delete_order(order_id: int, order_manager: IOrderManager = Depends(get_order_manager)):
    id_exist = order_manager.delete_order(order_id)
    if not id_exist:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found")
    
    return id_exist