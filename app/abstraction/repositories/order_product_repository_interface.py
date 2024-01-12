from abc import ABC, abstractmethod

from ...model.order_product import Order_product, Order_productValues

class IOrder_productRepository(ABC):
    @abstractmethod
    def read_orders_products(self) -> list[Order_product]:
        pass
    @abstractmethod
    def create_order_product(self, order_product: Order_productValues) -> Order_product:
        pass
    @abstractmethod
    def read_order_product(self, order_id: int) -> list[Order_product]:
        pass
    @abstractmethod
    def delete_order_product(self, order_id: int, product_id: int):
        pass
    @abstractmethod
    def update_order_product(self, order_to_be_updated_id: int, product_to_be_updated_id: int, amount: int):
        pass