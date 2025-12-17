from fastapi import APIRouter, Depends, HTTPException

from src.utils.db import get_db

from src.models.db import User

from src.models.api import UserResponse, CreateUserRequest

from src.crud.auth.dependencies import get_current_active_user

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/all", response_model=list[UserResponse])
async def get_all_users(current_user: User = Depends(get_current_active_user), db=Depends(get_db)):
    print(db)
    users = db.query(User).all()
    # return {
    #     "message": "list of all users",
    #     "users": users
    # }

    return users

@user_router.get("/me")
async def get_current_user():
    return {
        "message": "current user"
    }

@user_router.get("/specific/{user_id}", response_model=UserResponse)
async def specefic_user(user_id: int, current_user: User = Depends(get_current_active_user), db=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # return {
    #     "message": "specific user",
    #     "user": user
    # }

    return user

# @user_router.post("/new", response_model=UserResponse)
# async def create_user(user: CreateUserRequest, db=Depends(get_db)):
#     existing_user = db.query(User).filter(User.email == user.email).first()

#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already exists")
    
#     new_user = User(name=user.name, email=user.email, password=user.password)
    
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user
    
    # return {
    #     "message": "new user created",
    #     "user": new_user
    # }

@user_router.put("/update/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: CreateUserRequest, current_user: User = Depends(get_current_active_user), db=Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    existing_user.name = user.name
    existing_user.email = user.email
    # existing_user.password = user.password
    
    db.commit()
    db.refresh(existing_user)
    
    return {
        "message": "user updated",
        "user": existing_user
    }

@user_router.delete("/delete/{user_id}")
async def delete_user(user_id: int, current_user: User = Depends(get_current_active_user), db=Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(existing_user)
    db.commit()
    
    return {
        "message": "user deleted"
    }