from sqlalchemy import Column, Integer, String, Float, Table, MetaData

from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy import MetaData

metadata = MetaData()


Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)

# users = Table(
#     "users",
#     # metadata=metadata, # this will cause error
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("username", String),
#     # Column("email", String),
#     Column("password", String),
#     # metadata=metadata
# )

class User(Base):
    __tablename__ = "users"

    id=Column(Integer, primary_key=True, index=True)
    username=Column(String)
    # email=Column(String)
    password=Column(String)