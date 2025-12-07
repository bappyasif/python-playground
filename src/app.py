from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.db.models import User
from src.schemas.user import UserCreate, UserResponse, PatchUser
from src.utils.db import get_db
from src.crud.user import get_user, create_user, update_user, patch_user, delete_user

server = FastAPI(title="FastApi with PostgreSQL Database")

get_db()

@server.get("/")
def root():
    return {"message": "server running!!"}

@server.get("/users/{user_id}", response_model=UserResponse)
def get_a_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(user_id, db)

@server.post("/users/", response_model=UserResponse)
def create_a_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

# updating entire user details
@server.put("/users/{user_id}", response_model=UserResponse)
def update_a_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(user_id, user, db)

# updating partial user details
@server.patch("/users/{user_id}", response_model=UserResponse)
def patch_a_user(user_id: int, user: PatchUser, db: Session = Depends(get_db)):
    return patch_user(user_id, user, db)

@server.delete("/users/{user_id}")
def delete_a_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)

@server.get("/users/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users