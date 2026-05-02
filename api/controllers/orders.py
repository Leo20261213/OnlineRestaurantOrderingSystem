from sqlalchemy.orm import Session
from ..models.orders import Order
from ..schemas.orders import OrderCreate


def create_order(db: Session, order_in: OrderCreate) -> Order:
    db_order = Order(**order_in.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def list_orders(db: Session):
    return db.query(Order).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()