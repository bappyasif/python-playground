from collections.abc import AsyncGenerator
import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship

from datetime import datetime

from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTableUUID

from fastapi import Depends


# local database
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

class Base(DeclarativeBase):
    pass

# USER MODELS
class User(SQLAlchemyBaseUserTableUUID, Base):
    posts = relationship(argument="Post", back_populates="user") # relationship between user and post, user has many posts, post belongs to user

    # if we to have a foreign established on User side for anhy posts, it will be an example of many to one relationship, sa multiple user will have authorised for a single post

    # typically "child" table has a foreign key to "parent" table 


# DATA MODELS
class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False) # foreign key, user id is the primary key of the user table, user id is the id of the user who created the post, a reference to the user table
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship(argument="User", back_populates="posts") # relationship between user and post, user has many posts, post belongs to user, automatically links users and posts together in db and allows us to query posts by user, which is an example of one to many relationship

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)