from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import SessionLocal
from ..controllers.orders import create_order, list_orders, get_order
from ..schemas.orders import OrderCreate, OrderSchema

router = APIRouter(prefix="/orders", tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=OrderSchema)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)


@router.get("/", response_model=list[OrderSchema])
def list_orders_endpoint(db: Session = Depends(get_db)):
    return list_orders(db)


@router.get("/{order_id}", response_model=OrderSchema)
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order