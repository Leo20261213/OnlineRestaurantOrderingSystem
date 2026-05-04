from sqlalchemy import Column, Integer, String, Float
from FinalProject.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)