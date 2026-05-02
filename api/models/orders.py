from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from api.dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    total_amount = Column(Float, nullable=False)