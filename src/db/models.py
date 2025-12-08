from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)

    # password_hash = Column(String, nullable=False)
    # is_active = Column(Boolean, default=True)

# maybe something like this in future for authenticated users
# class AuthdUser(User):
#     __tablename__ = "authd_users"
    
#     password_hash = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)

# class AuthedUser(Base):
#     __tablename__ = "authed_users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     role = Column(String, index=True, nullable=False)

#     password_hash = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)