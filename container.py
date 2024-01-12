from fastapi import Depends
from app.abstraction.repositories.user_repository_interface import IUserRepository
from app.infrastructure.managers.user_manager import UserManager
from app.infrastructure.repositories.user_mysql_repository import UserMysqlRepository
from app.infrastructure.repositories.user_excel_repository import UserExcelRepository
from app.abstraction.repositories.product_repository_interface import IProductRepository
from app.infrastructure.managers.product_manager import ProductManager
from app.infrastructure.repositories.product_mysql_repository import ProductMysqlRepository
from app.abstraction.repositories.order_repository_interface import IOrderRepository
from app.infrastructure.managers.order_manager import OrderManager
from app.infrastructure.repositories.order_mysql_repository import OrderMysqlRepository
from app.abstraction.repositories.order_product_repository_interface import IOrder_productRepository
from app.infrastructure.managers.order_product_manager import Order_productManager
from app.infrastructure.repositories.order_product_mysql_repository import Order_productMysqlRepository

def get_user_repository():
    return UserMysqlRepository()

def get_user_manager(user_repository: IUserRepository = Depends(get_user_repository)):
    return UserManager(user_repository)

def get_product_repository():
    return ProductMysqlRepository()

def get_product_manager(product_repository: IProductRepository = Depends(get_product_repository)):
    return ProductManager(product_repository)

def get_order_repository():
    return OrderMysqlRepository()

def get_order_manager(order_repository: IOrderRepository = Depends(get_order_repository)):
    return OrderManager(order_repository)

def get_order_product_repository():
    return Order_productMysqlRepository()

def get_order_product_manager(order_product_repository: IOrder_productRepository = Depends(get_order_product_repository)):
    return Order_productManager(order_product_repository)