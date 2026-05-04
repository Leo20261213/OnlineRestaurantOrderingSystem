# FinalProject/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update with your actual MySQL credentials
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost/restaurant_db"

# Create the engine and session factory
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the Base for all models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()