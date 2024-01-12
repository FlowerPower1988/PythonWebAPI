from abc import ABC, abstractmethod

from ...model.product import Product, ProductValues

class IProductRepository(ABC):
    @abstractmethod
    def read_products(self) -> list[Product]:
        pass
    @abstractmethod
    def create_product(self, product: ProductValues) -> Product:
        pass
    @abstractmethod
    def read_product(self, product_id: int) -> Product:
        pass
    @abstractmethod
    def delete_product(self, product_id: int):
        pass
    @abstractmethod
    def update_product(self, product_to_be_updated_id: int ,new_values: ProductValues):
        pass