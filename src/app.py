from fastapi import FastAPI, Depends
from src.utils.db import get_session
from typing import Annotated
from sqlalchemy.orm import Session
from src.utils.db import create_db_and_tables
from contextlib import asynccontextmanager

SessionDep = Annotated[Session, Depends(get_session)]

server = FastAPI()

# @server.on_event("startup")
# async def startup():
#     await create_db_and_tables()

@asynccontextmanager
async def lifespan(server: FastAPI):
    create_db_and_tables()
    yield

server = FastAPI(lifespan=lifespan)

@server.get("/")
def root(session: SessionDep):
    return {"message": "server running!!", "session": session}