from sqlalchemy.orm import sessionmaker

from src.models.db import Base

from src.configs.db import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("tables created")
    except Exception as e:
        print(e)