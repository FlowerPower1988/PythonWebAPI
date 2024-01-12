from app.abstraction.repositories.order_manager_interface import IOrderManager
from app.abstraction.repositories.order_repository_interface import IOrderRepository
from ...model.order import OrderValues

class OrderManager(IOrderManager):

    def __init__(self, repo: IOrderRepository):
        self.repo = repo
    
    def read_orders(self):
        return self.repo.read_orders()

    def create_order(self, new_order_values: OrderValues):
        return self.repo.create_order(new_order_values)

    def read_order(self, order_id: int):
        return self.repo.read_order(order_id)
        
    def delete_order(self, order_id: int):
          return self.repo.delete_order(order_id)

    def update_order(self, order_to_be_updated_id: int, new_values: OrderValues):
        return self.repo.update_order(order_to_be_updated_id, new_values)
