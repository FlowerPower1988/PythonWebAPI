from fastapi import APIRouter, Depends, HTTPException
from app.abstraction.repositories.user_manager_interface import IUserManager
from container import get_user_manager
from ..model.user import  User, UserValues

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserValues, user_manager: IUserManager = Depends(get_user_manager)): 
    return user_manager.create_user(user)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, user_manager: IUserManager = Depends(get_user_manager)):
    
    user = user_manager.read_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    return user

@router.get("/users/", response_model=list[User])
def read_users(user_manager: IUserManager = Depends(get_user_manager)):
    return user_manager.read_users()

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_values: UserValues, user_manager: IUserManager = Depends(get_user_manager)):
    user = user_manager.update_user(user_id, user_values)
    
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    return user

@router.delete("/users/{user_id}", response_model=None)
def delete_user(user_id: int, user_manager: IUserManager = Depends(get_user_manager)):
    return user_manager.delete_user(user_id)