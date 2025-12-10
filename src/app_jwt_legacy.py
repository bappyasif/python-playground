from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from datetime import datetime, timedelta

# security configuartion
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

# now we need to create communication protocol between our db model and db
Base.metadata.create_all(bind=engine) # create the tables in the database

# Pydantic schemas, so that our api can communicate using these schemas
class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    
    class Config:
        # orm_mode = True # to work with sqlalchemy models (i.e. User) directly
        from_attributes = True # UserResponse class will use the attributes of the underlying SQLAlchemy model (User) to populate its own attributes when deserializing from a JSON payload

class PatchUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# helper functions for security
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        return TokenData(email=email)
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get_db()

# auth dependencies
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_access_token(token)
    user = db.query(User).filter(User.email == token_data.email).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist", headers={"WWW-Authenticate": "Bearer"})
    
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user

# auth endpoints
@server.post("/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user with the same email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password before storing it
    hashed_password = get_password_hash(user.password)
    
    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        hashed_password=hashed_password,
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@server.post("/token/", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    # Verify the password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=404, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@server.get("profile/", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user

@server.get("/verify-token/")
def verify_token(current_user: User = Depends(get_current_active_user)):
    return {
        "valid": True,
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email,
            "role": current_user.role,
            "is_active": current_user.is_active
        }
    }


# endpoints

@server.get("/")
def root():
    return {"message": "server running!!"}

@server.get("/users/", response_model=List[UserResponse])
def users_list(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@server.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int = 1, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        # return {"msg": "User found", "user": user} # as we are returning UserResponse as response model we'll have to return user object directly
        return user

@server.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    unique_user = db.query(User).filter(User.email == user.email).first()
    if unique_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # new_user = User(name=user.name, email=user.email, role=user.role)
    # new_user = User(**user.model_dump())
    # new_user = User(**user.dict())
    
    hashed_password = get_password_hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        hashed_password=hashed_password,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return {"msg": "New user created successfully", "user": new_user} # as we are not returning userid it will throw error as we have set response_model=UserResponse
    return {"msg": "New user created successfully", "user": UserResponse(id=new_user.id, **new_user.model_dump())}

# updating entire user details
@server.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
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
def delete_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if existing_user.id == current_user.id:
        raise HTTPException(status_code=400, detail="Users cannot delete themselves")

    db.delete(existing_user)
    db.commit()
    return {"msg": "User deleted successfully"}