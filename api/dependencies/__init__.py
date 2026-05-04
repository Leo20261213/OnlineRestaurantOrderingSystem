from sqlalchemy.orm import Session
from database import SessionLocal

# Dependency for database session management
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()