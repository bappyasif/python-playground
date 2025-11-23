from fastapi import FastAPI, HTTPException, File, UploadFile, Depends, Form

from src.db import get_async_session, create_db_and_tables, Post

from sqlalchemy.ext.asyncio import AsyncSession

from contextlib import asynccontextmanager

from sqlalchemy import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session) # dependency injection, it tells fastapi to inject the session object into the function so that it can be used inside the function, which is access to the database
):
    post = Post(
        caption= caption,
        url= "dummy_url",
        file_type= "dummy_photo",
        file_name= "dummy_name"
    )

    session.add(post) # add the post object to the session
    await session.commit() # commit the session to the database so that the post object is actually added to the database
    await session.refresh(post) # refresh the post object so that the id and other attributes are added to the post object
    return post # return the post object

@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    posts_data = []
    for post in posts:
        posts_data.append({
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })

    return {"posts": posts_data}
