from sqlalchemy import MetaData
from src.db.engine import engine
from sqlalchemy.orm import Session
from src.db.models import User
from sqlalchemy.exc import SQLAlchemyError
# from src.db.models import database_name

def create_db_and_tables():
    metadata = MetaData()
    metadata.create_all(bind=engine)

    # check if table exists and then create it if it doesnt exist
    try:
        engine.connect()
        print("Table already exists")
    except SQLAlchemyError:
        # Create the table if it doesn't exist
        with engine.connect() as connection:
            connection.execute(User.__table__.create())
            print("Table created successfully")


def get_session():
    with Session(engine) as session:
        yield session