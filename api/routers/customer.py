from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.schemas import CustomerCreate, CustomerResponse
from api.models import Customer
from api.dependencies import get_db

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    customer = Customer(**payload.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

@router.get("/", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, payload: CustomerCreate, db: Session = Depends(get_db)):
    customer = db.query(Customer).get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for field, value in payload.dict().items():
        setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).get(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()