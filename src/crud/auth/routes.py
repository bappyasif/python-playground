from fastapi import APIRouter, Depends, HTTPException, status

from src.models.api import CreateUserRequest

from src.models.db import User

from src.utils.db import get_db

from src.utils.jwt import get_password_hashed, verify_password, create_jwt_access_token

from src.crud.auth.dependencies import get_current_active_user

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta

from src.configs.jwt import ACCESS_TOKEN_EXPIRE_MINUTES

# auth_router = APIRouter(prefix="/user-auth", tags=["user-auth"])
auth_router = APIRouter(tags=["user-auth"])

@auth_router.post("/register")
async def register_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    # check if user with same email exists or not
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")
    
    print(existing_user)
    
    hashed_password = get_password_hashed(user.password)

    new_user = User(name=user.name, email=user.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "user registered",
        "user": new_user
    }

# @auth_router.post("/token") # moved to its own router
@auth_router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not active")
    
    # verify password
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    access_token = create_jwt_access_token(
        data={"sub": user.email},
        # expires_delta=int(timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)))
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    )
    
    return {
        "message": "user logged in successfully",
        "access_token": access_token,
        "token_type": "bearer"
    }

# @auth_router.post("/token")
@auth_router.post("/verify-token")
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