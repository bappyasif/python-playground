from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

# class User(BaseModel):
#     id: int
#     username: str
#     password: str