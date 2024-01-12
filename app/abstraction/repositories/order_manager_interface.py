from abc import ABC, abstractmethod

from ...model.order import Order, OrderValues

class IOrderManager(ABC):
    @abstractmethod
    def read_orders(self) -> list[Order]:
        pass
    @abstractmethod
    def create_order(self, new_order_values: OrderValues) -> Order:
        pass
    @abstractmethod
    def read_order(self, order_id: int) -> Order:
        pass
    @abstractmethod
    def delete_order(self, order_id: int):
        pass
    @abstractmethod
    def update_order(self, order_to_be_updated_id: int, new_values: OrderValues):
        pass