from app.abstraction.repositories.user_manager_interface import IUserManager
from app.abstraction.repositories.user_repository_interface import IUserRepository
from ...model.user import UserValues

class UserManager(IUserManager):

    def __init__(self, repo: IUserRepository):
        self.repo = repo
    
    def read_users(self):
        return self.repo.read_users()

    def create_user(self, new_user_values: UserValues):
        return self.repo.create_user(new_user_values)

    def read_user(self, user_id: int):
        return self.repo.read_user(user_id)
        
    def delete_user(self, user_id: int):
          return self.repo.delete_user(user_id)

    def update_user(self, user_to_be_updated_id: int, new_values: UserValues):
        return self.repo.update_user(user_to_be_updated_id, new_values)
