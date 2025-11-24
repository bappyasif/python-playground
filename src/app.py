from fastapi import FastAPI, HTTPException, File, UploadFile, Depends, Form

from src.db import get_async_session, create_db_and_tables, Post

from sqlalchemy.ext.asyncio import AsyncSession

from contextlib import asynccontextmanager

from sqlalchemy import select

from src.images import imagekit

from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

import shutil
import os
import uuid
import tempfile

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.delete("/posts/{post_id}")
async def delete_post(post_id: str, session: AsyncSession = Depends(get_async_session)):
    try:
        post_uuid = uuid.UUID(post_id)
        
        result = await session.execute(select(Post).where(Post.id == post_uuid))
        post = result.scalars().first()
        
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        
        await session.delete(post)
        await session.commit()
        
        return {"success": True, "message": "Post is deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/file-upload")
async def file_upload(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session) # dependency injection,
):
    temp_file_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

            upload_result = imagekit.upload_file(
                file=open(temp_file_path, "rb"),
                file_name=file.filename,
                options=UploadFileRequestOptions(
                    use_unique_file_name=True,
                    tags=["backend-upload"]
                )
            )

            # print(upload_result._UploadFileResult__response_metadata.http_status_code, "thit is status code")

            # return upload_result

            # print(upload_result.response_metadata.http_status_code, "thit is status code")

            # if upload_result.http_status_code == 200: # no good
            # if upload_result._UploadFileResult__response_metadata.http_status_code == 200: # good
            if upload_result.response_metadata.http_status_code == 200:
                post = Post(
                    caption= caption,
                    url= upload_result.url,
                    file_type= "video" if file.content_type.startswith("video") else "image",
                    file_name= upload_result.name
                )

                session.add(post) # add the post object to the session
                await session.commit() # commit the session to the database so that the post object is actually added to the database
                await session.refresh(post) # refresh the post object so that the id and other attributes are added to the post object
                # return post # return the post object but getting null?
                return {"id": str(post.id), "caption": post.caption, "url": post.url, "file_type": post.file_type, "file_name": post.file_name}
            else:
                raise HTTPException(status_code=upload_result.http_status_code, detail="Failed to upload file")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        file.file.close()


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
