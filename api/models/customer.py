from sqlalchemy import Column, Integer, String
from api.dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)