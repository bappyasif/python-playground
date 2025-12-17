from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.models.api import AuthdTokenRequest
from src.models.db import User
from src.configs.jwt import oauth2_scheme
from src.utils.jwt import verify_jwt_access_token

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_jwt_access_token(token)

    user = db.query(User).filter(User.email == token_data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
    return user

def get_current_active_user(current_user: AuthdTokenRequest = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user