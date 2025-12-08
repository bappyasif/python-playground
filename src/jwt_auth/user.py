from fastapi.security import oauth2
from typing import Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = oauth2.OAuth2PasswordBearer(tokenUrl="token")