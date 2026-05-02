# api/models/model_loader.py
from ..dependencies.database import Base, engine
from . import customer, menu_item, orders, order_details, payment, admin, restaurant_staff  # noqa: F401

def index():
    Base.metadata.create_all(bind=engine)