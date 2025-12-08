from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from src.db.models import User
from src.schemas.user import UserCreate
from src.utils.auth import create_access_token, get_current_active_user
from src.utils.db import get_db
from src.utils.auth import get_password_hash, verify_password
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.jwt_auth.user import ACCESS_TOKEN_EXPIRE_MINUTES as TOKEN_EXPIRE_MINUTES

def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user

def verify_token(current_user: User = Depends(get_current_active_user)):
    return {
        "valid": True,
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email,
            "role": current_user.role,
            "is_active": current_user.is_active
        }
    }

def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user with the same email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password before storing it
    hashed_password = get_password_hash(user.password)
    
    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        password_hash=hashed_password,
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    # Verify the password
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=404, detail="Incorrect email or password")
    
    expire_token_exires = timedelta(minutes=TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=expire_token_exires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

# def login_for_access_token(email: str, password: str, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.email == email).first()
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
    
#     # Verify the password
#     if not verify_password(password, user.password_hash):
#         raise HTTPException(status_code=404, detail="Incorrect email or password")
    
#     return user