from abc import ABC, abstractmethod

from ...model.user import User, UserValues

class IUserRepository(ABC):
    @abstractmethod
    def read_users(self) -> list[User]:
        pass
    @abstractmethod
    def create_user(self, user: UserValues) -> User:
        pass
    @abstractmethod
    def read_user(self, user_id: int) -> User:
        pass
    @abstractmethod
    def delete_user(self, user_id: int):
        pass
    @abstractmethod
    def update_user(self, user_to_be_updated_id: int ,new_values: UserValues):
        pass