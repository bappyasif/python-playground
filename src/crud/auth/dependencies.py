from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.models.db_tables import User
from src.configs.jwt import oauth2_scheme
from src.utils.auth import verify_access_token

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_access_token(token)
    user = db.query(User).filter(User.email == token_data.email).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist", headers={"WWW-Authenticate": "Bearer"})
    
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user