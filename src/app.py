from fastapi import FastAPI
from src.crud.user.routes import user_router
from src.crud.auth.routes import auth_router
from src.utils.db import create_tables

server = FastAPI()

server.include_router(user_router, prefix="/api/v1")

server.include_router(auth_router, prefix="/api/v1")

# Define a decorator to call create_tables when the server starts
def on_start(func):
    def wrapper():
        create_tables()
        func()
    return wrapper

# this wont work as decorator function expects a function as a parameter
# def on_start():
#     create_tables() 

# Apply the decorator to the FastAPI route or other initialization code
@server.get("/")
@on_start
def root():
    return {"message": "server and db running!!"}