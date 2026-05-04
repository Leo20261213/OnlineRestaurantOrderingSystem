from pydantic import BaseModel, ConfigDict

class OrderItemCreate(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    menu_item_id: int
    quantity: int

    # Updated for Pydantic v2
    model_config = ConfigDict(from_attributes=True)