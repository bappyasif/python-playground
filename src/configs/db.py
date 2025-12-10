from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database setup using postgresql
# make a dictionary where required db credentials are stored
db = {
    "username": "root",
    "password": "1234",
    "host": "localhost",
    "database": "jodb"
}

# DATABASE_URL = "postgresql://root:1234@localhost/jodb" # unless you have manually created a db named jodb it will throw error when trying to connect
DATABASE_URL = f"postgresql://{db['username']}:{db['password']}@{db['host']}/{db['database']}"

engine = create_engine(
        DATABASE_URL, 
        # echo=True, # log sql queries
        # connect_args={"check_same_thread": False} # only for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)