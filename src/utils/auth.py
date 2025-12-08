from src.jwt_auth.user import pwd_context
from typing import Optional
from datetime import timedelta, datetime
import jwt
from src.jwt_auth.user import SECRET_KEY, ALGORITHM
from src.schemas.user import TokenData
from fastapi import HTTPException, status, Depends
from src.utils.db import get_db
from src.jwt_auth.user import oauth2_scheme
from sqlalchemy.orm import Session
from src.db.models import User



def verify_password(plain_password: str, hashed_password: str) -> bool:
    # """Verify a plain password against its hashed version."""
    # Implementation goes here
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    # """Hash a plain password."""
    # Implementation goes here
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            # raise ValueError("Invalid token: missing subject")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        return TokenData(email=email)
    except jwt.PyJWTError:
        # raise ValueError("Could not validate credentials")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except ValueError as e:
        raise ValueError(str(e))
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> TokenData:
    token_data = verify_token(token)
    user = db.query(User).filter(User.email == token_data.email).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist", headers={"WWW-Authenticate": "Bearer"})
    
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user