from sqlalchemy import create_engine
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import sessionmaker

# Database configuration
username = 'myuser'
password = '1234'
host = 'localhost'
port = 5432
database_name = 'localdb'

# Create the engine
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database_name}')

# Session = sessionmaker(bind=engine)
# session = Session()


# Check if the database exists
# try:
#     engine.connect()
#     print("Database already exists")
# except SQLAlchemyError:
#     # Create the database if it doesn't exist
#     with engine.connect() as connection:
#         connection.execute(f"CREATE DATABASE {database_name}")
#         print(f"Database {database_name} created successfully")

# from sqlalchemy import create_engine
# from sqlalchemy.exc import SQLAlchemyError

# database_name = "localdb"

# DATABASE_URL = "postgresql://myuser:1234@localhost:5432/"+database_name

# # engine = create_engine(DATABASE_URL, {"check_same_thread": False})
# engine = create_engine(DATABASE_URL)

# # Check if the database exists
# try:
#     engine.connect()
#     print("Database already exists")
# except SQLAlchemyError:
#     # Create the database if it doesn't exist
#     with engine.connect() as connection:
#         connection.execute(f"CREATE DATABASE {database_name}")
#         print(f"Database {database_name} created successfully")