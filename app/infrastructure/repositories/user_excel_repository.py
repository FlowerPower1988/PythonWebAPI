from ...abstraction.repositories.user_repository_interface import IUserRepository
from ...model.user import User, UserValues
import pandas as pd


class UserExcelRepository(IUserRepository):
    def read_users(self):
        path = "C:/Users/adelh/OneDrive/Documents/GitHub/PythonWebAPI/app/infrastructure/repositories/users.xlsx"
        df = pd.read_excel(path, sheet_name='Sheet1')
        users = df.values.tolist()
        user_list=[]
        for user in users:
            new_user = User(id=user[0], name=user[1], email=user[2])
            user_list.append(new_user)
        return user_list
    
    def read_user(self, user_id: int):
        path = "C:/Users/adelh/OneDrive/Documents/GitHub/PythonWebAPI/app/infrastructure/repositories/users.xlsx"
        df = pd.read_excel(path, sheet_name='Sheet1')
        users = df.values.tolist()
        for i in range(len(users)):
            if user_id in users[i]:
                user = User(id=users[i][0], name=users[i][1], email=users[i][2])             
                return user
        return False
    
    def create_user(self, new_user_values: UserValues):
        path="C:/Users/adelh/OneDrive/Documents/GitHub/PythonWebAPI/app/infrastructure/repositories/users.xlsx"
        df = pd.read_excel(path, sheet_name='Sheet1')
        users = df.values.tolist()
        user_list=[]
        for user in users:
            next_user = User(id=user[0], name=user[1], email=user[2])
            user_list.append(next_user)

        user_with_highest_id = max(user_list, key=lambda obj: obj.id, default=None)
        highest_id = user_with_highest_id.id  if user_with_highest_id is not None else 0
        new_user_id = (highest_id or 0) + 1 
        new_user = {'id': new_user_id, 'user_name': new_user_values.name, 'email': new_user_values.email}
        
        for column, value in new_user.items():
            index = len(user_list)
            df.at[index, column] = value
        df.to_excel(path, index=False)
        
        new_user_obj = User(id=new_user['id'], name=new_user['user_name'], email=new_user['email'])
        return new_user_obj
    
    def delete_user(self, user_id: int):
        path="C:/Users/adelh/OneDrive/Documents/GitHub/PythonWebAPI/app/infrastructure/repositories/users.xlsx"
        df = pd.read_excel(path, sheet_name='Sheet1')
        users = df.values.tolist()
        for i in range(len(users)):
            if user_id in users[i]:
                index = i
                df.drop([index],axis=0,inplace=True)
                df.to_excel(path, index=False)
                return True
        return False
        
        
    def update_user(self, user_to_be_updated_id: int ,new_values: UserValues):
        path="C:/Users/adelh/OneDrive/Documents/GitHub/PythonWebAPI/app/infrastructure/repositories/users.xlsx"
        df = pd.read_excel(path, sheet_name='Sheet1')
        users = df.values.tolist()
        for i in range(len(users)):
            if user_to_be_updated_id in users[i]:
                index = i
                new_user = {'id': user_to_be_updated_id, 'user_name': new_values.name, 'email': new_values.email}
                for column, value in new_user.items():
                    df.at[index, column] = value
                df.to_excel(path, index=False)
                new_user_obj = User(id=user_to_be_updated_id, name=new_values.name, email=new_values.email)
                return new_user_obj
        return False

        