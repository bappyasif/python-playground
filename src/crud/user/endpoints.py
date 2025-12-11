from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.models.db_tables import User
from src.models.api_schemas import UserCreate, UserResponse, PatchUser
from src.crud.auth.dependencies import get_current_active_user
from src.utils.auth import get_password_hash

def users_list(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

def get_user(user_id: int = 1, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        # return {"msg": "User found", "user": user} # as we are returning UserResponse as response model we'll have to return user object directly
        return user
    

def create_user(user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    unique_user = db.query(User).filter(User.email == user.email).first()
    if unique_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # new_user = User(name=user.name, email=user.email, role=user.role)
    # new_user = User(**user.model_dump())
    # new_user = User(**user.dict())
    
    hashed_password = get_password_hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        hashed_password=hashed_password,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return {"msg": "New user created successfully", "user": new_user} # as we are not returning userid it will throw error as we have set response_model=UserResponse
    return {"msg": "New user created successfully", "user": UserResponse(id=new_user.id, **new_user.model_dump())}

def update_user(user_id: int, user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    #     existing_user.name = user.name
    #     existing_user.email = user.email
    #     existing_user.role = user.role

    for key, val in user.model_dump().items():
        setattr(existing_user, key, val)

    db.commit()
    db.refresh(existing_user)
    return existing_user

def patch_user(user_id: int, user: PatchUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    # if user.name:
    #     existing_user.name = user.name
    # if user.email:
    #     existing_user.email = user.email
    # if user.role:
    #     existing_user.role = user.role
    for key, val in user.model_dump().items():
        if val is not None:
            setattr(existing_user, key, val)
    db.commit()
    db.refresh(existing_user)
    return existing_user

def delete_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if existing_user.id == current_user.id:
        raise HTTPException(status_code=400, detail="Users cannot delete themselves")

    db.delete(existing_user)
    db.commit()
    return {"msg": "User deleted successfully"}