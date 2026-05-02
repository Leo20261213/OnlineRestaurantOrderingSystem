from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerSchema(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True