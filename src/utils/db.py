from sqlalchemy import MetaData
from src.db.engine import engine
from sqlalchemy.orm import Session
from src.db.models import User, Task
from sqlalchemy.exc import SQLAlchemyError
# from src.db.models import database_name
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def table_exists(table_name):
    inspector = inspect(engine)
    return inspector.has_table(table_name)

def create_db():
    # create database if it doiesnt exist
    metadata = MetaData()
    metadata.create_all(bind=engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # Base.metadata.create_all(engine)
    # print("Database created successfully")
    

# def create_tables():
#     # check if table exists and then create it if it doesnt exist
#     try:
#         engine.connect()
#         print("Table already exists")
#     except SQLAlchemyError:
#         # Create the table if it doesn't exist
#         with engine.connect() as connection:
#             connection.execute(User.__table__.create())
#             connection.execute(Task.__table__.create())
#             print("Tables created successfully")

def create_tables():
    if not table_exists('users'):
        with engine.begin() as connection:
            connection.execute(User.__table__.create(bind=engine))
    
    if not table_exists('tasks'):
        with engine.begin() as connection:
            connection.execute(Task.__table__.create(bind=engine))
    # if not table_exists('users'):
    #     with engine.begin() as connection:
    #         connection.execute(User.__table__.create(bind=engine))
    #         connection.execute(Task.__table__.create(bind=engine))

def create_db_and_tables():
    # metadata = MetaData()
    # metadata.create_all(bind=engine)
    # create_db() # we are creating db using cmd before hand
    create_tables()

    # check if table exists and then create it if it doesnt exist
    # try:
    #     engine.connect()
    #     print("Table already exists")
    # except SQLAlchemyError:
    #     # Create the table if it doesn't exist
    #     with engine.connect() as connection:
    #         connection.execute(User.__table__.create())
    #         connection.execute(Task.__table__.create())
    #         print("Tables created successfully")


# engine = create_async_engine(settings.db_dsn, echo=True, future=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, class_=AsyncSession, future=True)

def get_session():
    with Session(engine) as session:
        print ("Getting session...", session)
        yield session

# async def get_session():
#     async with SessionLocal() as session:
#         yield session