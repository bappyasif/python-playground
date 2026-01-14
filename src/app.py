from fastapi import FastAPI
from src.crud.user.routes import user_router
from src.crud.auth.routes import auth_router
from src.crud.auth.endpoint import auth_token_router
from src.huggingface.inference import hfi_router
from src.utils.db import create_tables
# from src.huggingface.hf_hub import hf_hub_download
# import src.huggingface.hf_req
import src.huggingface.hf_hub_try_II 
import src.huggingface.hf_hub
from src.crud.genai.routes import genai_router

server = FastAPI()

server.include_router(user_router, prefix="/api/v1")

server.include_router(auth_router, prefix="/api/v1")

# when using "Authorize" its trying to locate "/token" endpoint using prefix makes it harder or unfindable, so kept it in a separate router to keep it special and distinct for understanding
server.include_router(auth_token_router)

server.include_router(hfi_router, prefix="/api/v1")

server.include_router(genai_router, prefix="/api/v1")

# Define a decorator to call create_tables when the server starts
def on_start(func):
    def wrapper():
        create_tables()
        func()
    return wrapper

# Apply the decorator to the FastAPI route or other initialization code
@server.get("/")
@on_start
def root():
    return {"message": "server and db running!!"}