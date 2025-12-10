from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://root:1234@localhost/jodb" # unless you have manually created a db named jodb it will throw error when trying to connect

engine = create_engine(
        DATABASE_URL, 
        echo=True, # log sql queries
        # connect_args={"check_same_thread": False} # only for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)