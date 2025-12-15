from fastapi import APIRouter, Depends

from src.utils.db import get_db

from src.models.db import User

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/all")
async def get_all_users(db=Depends(get_db)):
    print(db)
    users = db.query(User).all()
    return {
        "message": "list of all users"
    }

@user_router.get("/me")
async def get_current_user():
    return {
        "message": "current user"
    }