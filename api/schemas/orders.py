from pydantic import BaseModel, ConfigDict

class OrderCreate(BaseModel):
    customer_id: int
    total_amount: float
    status: str | None = None


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: float
    status: str | None = None

    model_config = ConfigDict(from_attributes=True)