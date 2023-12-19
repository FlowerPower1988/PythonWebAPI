
from ...abstraction.repositories.user_repository_interface import IUserRepository
from ...model.user import User, UserValues

users: list[User] = []

class PostStaicRepository(IUserRepository):
    def read_users(self):
        return users

    def create_user(self, new_user_values: UserValues):
        user_with_highest_id = max(users, key=lambda obj: obj.id, default=None) 
        highest_id = user_with_highest_id.id  if user_with_highest_id is not None else 0
        new_user_id = (highest_id or 0) + 1
        new_user: User = User(id=new_user_id, **new_user_values.__dict__)
        users.append(new_user)
        return new_user

    def read_user(self, user_id: int):
        matching_users = [user for user in users if user.id == user_id]
        return matching_users[0] if matching_users else None
        
    def delete_user(self, user_id: int):
        result = False
        user = next((user for user in users if user.id == user_id), None)
       
        if user:
            users.remove(user)
            result = True
        return result
    
    def update_user(self, user_to_be_updated_id: int ,new_values: UserValues):
        user = next((user for user in users if user.id == user_to_be_updated_id), None)
       
        if user:
            user.name = new_values.name
            user.email = new_values.name
        return user
