from sqlalchemy import Column, Integer, String
from api.dependencies.database import Base

class RestaurantStaff(Base):
    __tablename__ = "restaurant_staff"

    staff_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    email = Column(String(150), unique=True, nullable=False)