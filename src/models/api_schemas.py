from pydantic import BaseModel
from typing import Optional

# Pydantic schemas, so that our api can communicate using these schemas
class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    
    class Config:
        # orm_mode = True # to work with sqlalchemy models (i.e. User) directly
        from_attributes = True # UserResponse class will use the attributes of the underlying SQLAlchemy model (User) to populate its own attributes when deserializing from a JSON payload

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