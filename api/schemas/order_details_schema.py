from pydantic import BaseModel

class OrderDetailsBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int
    subtotal: float

class OrderDetailsCreate(OrderDetailsBase):
    pass

class OrderDetailsSchema(OrderDetailsBase):
    class Config:
        orm_mode = True