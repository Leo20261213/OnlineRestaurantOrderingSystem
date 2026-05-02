from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    amount: float
    payment_type: str
    transaction_status: str

class PaymentCreate(PaymentBase):
    pass

class PaymentSchema(PaymentBase):
    payment_id: int

    class Config:
        from_attributes = True