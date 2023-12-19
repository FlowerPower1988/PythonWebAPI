from fastapi import Depends
from app.abstraction.repositories.user_repository_interface import IUserRepository
from app.infrastructure.managers.user_manager import UserManager
from app.infrastructure.repositories.user_mysql_repository import UserMysqlRepository

def get_user_repository():
    return UserMysqlRepository()

def get_user_manager(user_repository: IUserRepository = Depends(get_user_repository)):
    return UserManager(user_repository)