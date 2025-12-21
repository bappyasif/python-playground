from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from src.configs.jwt import ACCESS_TOKEN_EXPIRE_MINUTES
from src.utils.db import get_db
from src.utils.jwt import create_jwt_access_token, verify_password
from src.models.db import User

auth_token_router = APIRouter(tags=["auth-token"])

@auth_token_router.post("/token")
async def authorize_user_Oauth2_Form(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
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
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    )
    
    return {
        "message": "user logged in successfully",
        "access_token": access_token,
        "token_type": "bearer"
    }