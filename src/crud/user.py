from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from src.schemas.user import UserCreate, PatchUser
from src.utils.db import get_db
from src.db.models import User

def get_user(user_id, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, val in user.model_dump().items():
        setattr(existing_user, key, val)
    db.commit()
    db.refresh(existing_user)
    return existing_user

def patch_user(user_id: int, user: PatchUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, val in user.model_dump().items():
        if val is not None:
            setattr(existing_user, key, val)
    db.commit()
    db.refresh(existing_user)
    return existing_user

def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(existing_user)
    db.commit()
    return {"msg": "User deleted successfully"}