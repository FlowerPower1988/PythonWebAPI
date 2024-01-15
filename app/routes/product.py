from fastapi import APIRouter, Depends, HTTPException
from app.abstraction.repositories.product_manager_interface import IProductManager
from container import get_product_manager
from ..model.product import  Product, ProductValues

router2 = APIRouter()

@router2.post("/products/", response_model=Product)
def create_product(product: ProductValues, product_manager: IProductManager = Depends(get_product_manager)): 
    return product_manager.create_product(product)

@router2.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, product_manager: IProductManager = Depends(get_product_manager)):
    
    product = product_manager.read_product(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    
    return product

@router2.get("/products/", response_model=list[Product])
def read_products(product_manager: IProductManager = Depends(get_product_manager)):
    return product_manager.read_products()

@router2.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_values: ProductValues, product_manager: IProductManager = Depends(get_product_manager)):
    product = product_manager.update_product(product_id, product_values)
    
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    
    return product

@router2.delete("/products/{product_id}", response_model=None)
def delete_product(product_id: int, product_manager: IProductManager = Depends(get_product_manager)):
    id_exist = product_manager.delete_product(product_id)
    if not id_exist:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
    elif id_exist==409:
        raise HTTPException(status_code=409, detail=f"Product with ID {product_id} has been ordered")
    return id_exist