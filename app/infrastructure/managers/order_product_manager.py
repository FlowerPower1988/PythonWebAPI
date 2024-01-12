from app.abstraction.repositories.order_product_manager_interface import IOrder_productManager
from app.abstraction.repositories.order_product_repository_interface import IOrder_productRepository
from ...model.order_product import Order_productValues

class Order_productManager(IOrder_productManager):

    def __init__(self, repo: IOrder_productRepository):
        self.repo = repo
    
    def read_orders_products(self):
        return self.repo.read_orders_products()

    def create_order_product(self, new_order_product_values: Order_productValues):
        return self.repo.create_order_product(new_order_product_values)

    def read_order_product(self, order_id: int):
        return self.repo.read_order_product(order_id)
        
    def delete_order_product(self, order_id: int, product_id: int):
          return self.repo.delete_order_product(order_id, product_id)

    def update_order_product(self, order_to_be_updated_id: int, product_to_be_updated_id: int, amount: int):
        return self.repo.update_order_product(order_to_be_updated_id, product_to_be_updated_id, amount)
