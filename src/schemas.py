from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    # id: int = None

class PostResponse(PostCreate):
    id: int