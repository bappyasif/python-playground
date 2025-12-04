from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# metadata = MetaData()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=True)
    description = Column(String, index=True, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="tasks")

class User(Base):
    __tablename__ = "users"

    # metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

# if i dont keep it above User class on initial it only creates User table in db not Taskj table
# class Task(Base):
#     __tablename__ = 'tasks'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True, nullable=True)
#     description = Column(String, index=True, nullable=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     user = relationship("User", back_populates="tasks")