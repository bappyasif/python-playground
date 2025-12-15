from fastapi import APIRouter

auth_router = APIRouter(prefix="/user-auth", tags=["user-auth"])

@auth_router.post("/register")
async def register_user():
    return {
        "message": "user registered"
    }

@auth_router.post("/login")
async def login_user():
    return {
        "message": "user logged in"
    }