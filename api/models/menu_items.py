from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)

    # Add this line to fix the mapper error
    order_items = relationship("OrderItem", back_populates="menu_item")