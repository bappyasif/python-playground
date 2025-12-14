from fastapi import FastAPI

server = FastAPI()

@server.get("/")
def root():
    return {"message": "server running!!"}