from fastapi import FastAPI, Depends
from src.utils.db import get_session
from typing import Annotated
from sqlalchemy.orm import Session
from src.utils.db import create_db_and_tables
from contextlib import asynccontextmanager

SessionDep = Annotated[Session, Depends(get_session)]

# server = FastAPI()

# @server.on_event("startup")
# async def startup():
#     await create_db_and_tables()

@asynccontextmanager
async def lifespan(server: FastAPI):
    yield create_db_and_tables()
    

server = FastAPI(lifespan=lifespan)

@server.get("/")
def root(
    session: SessionDep
    # session: Session = Depends(get_session)
    # session: Session = Depends(get_session)
):
    # sess = get_session()
    # session_id = sess.session_id
    # session_status = sess.status

    # print("Session ID:", session_id)
    # print("Session Status:", session_status)

    # session_dict = session.as_dict()
    # session.query(User).first()
    print("Session in root...", session)
    # return {"message": "server running!!", "session": {"session_id": session.session_id, "session_status": session.status}}
    # return {"message": "server running!!", "session": {"session_id": session.connection._connection._connection_id, "session_status": session.status}}
    return {"message": "server running!!", "session": session or "no session"}