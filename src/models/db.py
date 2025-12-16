from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    token = Column(String, unique=True, index=True)


# class AuthdUser(User):
#     __tablename__ = "authd_users"

#     token = Column(String, unique=True, index=True)
#     # refresh_token = Column(String, unique=True, index=True)
#     isActiveUser = Column(Boolean, default=True)