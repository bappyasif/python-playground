from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.auth.schemas import CreateUser, LoginUser
# from src.schemas import *
from bcrypt import hashpw, gensalt, checkpw
import src.db_models
from src.utils.init import get_db

def register_user(user: CreateUser, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        return {"message": "User already exists"}
    else:
        salt = gensalt()
        hashed_password = hashpw(user.password.encode('utf-8'), salt)

        # transform bytes to string
        hashed_password = hashed_password.decode('utf-8') # without this conversion it will throw error as bytes object is not verifyable against string

        new_user = src.db_models.User(username=user.username, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created", "user": new_user, "hashed_password": hashed_password, "salt": salt}
    
def register_user_without_hashing(user: CreateUser, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        return {"message": "User already exists"}
    else:
        new_user = src.db_models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created", "user": new_user}
    
def user_login_without_hashing(user: LoginUser, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        if query.password == user.password:
            return {"message": "Login successful"}
        else:
            return {"message": "Incorrect password"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
def verify_password(password: str, hashed_password: str) -> bool:
    return checkpw(password.encode(), hashed_password.encode())
    
def user_login(user: LoginUser, db: Session = Depends(get_db)):
    query = db.query(src.db_models.User).filter(src.db_models.User.username == user.username).first()

    if query:
        if verify_password(user.password, query.password):
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    else:
        raise HTTPException(status_code=404, detail="User not found")