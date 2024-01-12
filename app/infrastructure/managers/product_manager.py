from app.abstraction.repositories.product_manager_interface import IProductManager
from app.abstraction.repositories.product_repository_interface import IProductRepository
from ...model.product import ProductValues

class ProductManager(IProductManager):

    def __init__(self, repo: IProductRepository):
        self.repo = repo
    
    def read_products(self):
        return self.repo.read_products()

    def create_product(self, new_product_values: ProductValues):
        return self.repo.create_product(new_product_values)

    def read_product(self, product_id: int):
        return self.repo.read_product(product_id)
        
    def delete_product(self, product_id: int):
          return self.repo.delete_product(product_id)

    def update_product(self, product_to_be_updated_id: int, new_values: ProductValues):
        return self.repo.update_product(product_to_be_updated_id, new_values)
