from typing import Optional

from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True # UserResponse class will use the attributes of the underlying SQLAlchemy model (User) to populate its own attributes when deserializing from a JSON payload

class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    password: str

class PatchUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None