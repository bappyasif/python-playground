from typing import Optional

from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True # UserResponse class will use the attributes of the underlying SQLAlchemy model (User) to populate its own attributes when deserializing from a JSON payload

class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class PatchUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None

