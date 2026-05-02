from sqlalchemy import Column, Integer, Float, ForeignKey
from api.dependencies.database import Base

class OrderDetails(Base):
    __tablename__ = "order_details"

    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)