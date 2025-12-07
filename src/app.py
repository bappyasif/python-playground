from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional

server = FastAPI(title="FastApi with PostgreSQL Database")

# Database setup using postgresql
DATABASE_URL = "postgresql://root:1234@localhost/jodb" # unless you have manually created a db named jodb it will throw error when trying to connect
engine = create_engine(
        DATABASE_URL, 
        echo=True, # log sql queries
        # connect_args={"check_same_thread": False} # only for sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()

# Database models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)

# now we need to create communication protocol between our db model and db
Base.metadata.create_all(bind=engine) # create the tables in the database

# Pydantic schemas, so that our api can communicate using these schemas
class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    
    class Config:
        # orm_mode = True # to work with sqlalchemy models (i.e. User) directly
        from_attributes = True # UserResponse class will use the attributes of the underlying SQLAlchemy model (User) to populate its own attributes when deserializing from a JSON payload

class PatchUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()

@server.get("/")
def root():
    return {"message": "server running!!"}

@server.get("/users/{user_id}", response_model=UserResponse)
def get_user(db: Session = Depends(get_db), user_id: int = 1):
    user = db.query(User).filter(User.id == user_id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        # return {"msg": "User found", "user": user} # as we are returning UserResponse as response model we'll have to return user object directly
        return user

@server.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    unique_user = db.query(User).filter(User.email == user.email).first()
    if unique_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # new_user = User(name=user.name, email=user.email, role=user.role)
    # new_user = User(**user.model_dump())
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return {"msg": "New user created successfully", "user": new_user} # as we are not returning userid it will throw error as we have set response_model=UserResponse
    return {"msg": "New user created successfully", "user": UserResponse(id=new_user.id, **new_user.model_dump())}

# updating entire user details
@server.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    #     existing_user.name = user.name
    #     existing_user.email = user.email
    #     existing_user.role = user.role

    for key, val in user.model_dump().items():
        setattr(existing_user, key, val)
    db.commit()
    db.refresh(existing_user)
    return existing_user

# updating partial user details
@server.patch("/users/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, user: PatchUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    # if user.name:
    #     existing_user.name = user.name
    # if user.email:
    #     existing_user.email = user.email
    # if user.role:
    #     existing_user.role = user.role
    for key, val in user.model_dump().items():
        if val is not None:
            setattr(existing_user, key, val)
    db.commit()
    db.refresh(existing_user)
    return existing_user

@server.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(existing_user)
    db.commit()
    return {"msg": "User deleted successfully"}

@server.get("/users/", response_model=List[UserResponse])
def users_list(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users