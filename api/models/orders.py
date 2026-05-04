from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  # ← must exist
    customer_id = Column(Integer, ForeignKey("customers.id"))
    total_amount = Column(Float)
    status = Column(String(50), default="pending")

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
