from src.db import SessionLocal, engine
from sqlalchemy.orm import DeclarativeBase

def get_db():
    db = SessionLocal()

    try:
        yield db
    
    except Exception as e:
        raise e
            
    finally:
        db.close()
    

# this is something that i saw in a buffed up tutorial seemed quite useful to me and could be used for future projects
class Base(DeclarativeBase):
    pass

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)