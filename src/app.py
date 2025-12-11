from fastapi import FastAPI, Depends
from typing import List
from src.models.api_schemas import UserResponse, PatchUser, UserCreate, Token
from src.models.db_tables import User
from src.crud.auth.dependencies import get_current_active_user
from src.crud.auth.endpoints import get_profile, register_user, login_user, verify_token
from src.crud.user.endpoints import users_list, get_user, create_user, update_user, delete_user, patch_user
from src.utils.db import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from src.utils.db import init_db

server = FastAPI(title="FastApi with PostgreSQL Database") # this works

# Create all tables in the database if they don't already exist
# This is a one-time operation, so it's usually done once in the main application file
# You can also do it in a separate file, like in the "src/configs/db.py" file
# But if you do it there, you'll have to import "Base" from "src/models/db_tables.py" into "src/configs/db.py"
# And then you'll have to import "engine" from "src/configs/db.py" into your main application file
# So it's usually easier to just do it here in the main application file

# Base.metadata.create_all(bind=engine)
init_db() # this works regardless of when tables are not created upfront

# @server.on_event("startup") # depricated
# def init_db_event():
#     init_db()

# @lifecycle.on_event("startup")
# def init_db_event():
#     init_db()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     init_db()
#     yield

# server = FastAPI(title="FastApi with PostgreSQL Database", lifespan=lifespan)

@server.get("/")
def root():
    return {"message": "server running!!"}

# Users CRUD
@server.get("/users/", response_model=List[UserResponse])
def all_users(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return users_list(current_user, db)

@server.get("/users/{user_id}", response_model=UserResponse)
def get_a_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return get_user(user_id, current_user, db)

@server.post("/users/", response_model=UserResponse)
def create_a_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return create_user(user_id, current_user, db)   

@server.put("/users/{user_id}", response_model=UserResponse)
def update_a_user(user_id: int, user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return update_user(user_id, user, current_user, db)

@server.patch("/users/{user_id}", response_model=UserResponse)
def patch_a_user(user_id: int, user: PatchUser, db: Session = Depends(get_db)):
    return patch_user(user_id, user, db)

@server.delete("/users/{user_id}")
def delete_a_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return delete_user(user_id, current_user, db)

# Authentication
@server.post("/register/", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@server.post("/token/", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_user(form_data, db)

@server.get("/profile/", response_model=UserResponse)
def get_current_profile(current_user: User = Depends(get_current_active_user)):
    return get_profile(current_user=current_user)

@server.get("/verify-token")
def verify_user_token(current_user: User = Depends(get_current_active_user)):
    return verify_token(current_user=current_user)