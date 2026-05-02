from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from api.dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    method = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)