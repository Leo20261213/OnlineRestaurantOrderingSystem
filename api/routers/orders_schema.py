from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    customer_id: int
    order_date: datetime
    status: str
    total_amount: float

class OrderCreate(OrderBase):
    pass

class OrderSchema(OrderBase):
    order_id: int

    class Config:
        orm_mode = True