from pydantic import BaseModel
from typing import Optional

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    class Config:
        # orm_mode = True
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    username: str
    token: str

class AuthdTokenRequest(BaseModel):
    email: Optional[str] = None

class AuthdTokenResponse(BaseModel):
    token: str