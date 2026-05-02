from sqlalchemy import Column, Integer, String
from api.dependencies.database import Base

class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)