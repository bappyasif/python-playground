from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# postgres db config object required for fastapi
db_dict = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'root',
    'password': '1234',
    'database': 'jodb'
}

# Database setup using postgresql
# DATABASE_URL = "postgresql://root:1234@localhost/jodb" # unless you have manually created a db named jodb it will throw error when trying to connect
DATABASE_URL = f"{db_dict['drivername']}://{db_dict['username']}:{db_dict['password']}@{db_dict['host']}/{db_dict['database']}"

engine = create_engine(
        DATABASE_URL, 
        # echo=True, # log sql queries
        # connect_args={"check_same_thread": False} # only for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)