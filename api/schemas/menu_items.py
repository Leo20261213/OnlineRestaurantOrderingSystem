from pydantic import BaseModel, ConfigDict

class MenuItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float


class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

    # Updated for Pydantic v2
    model_config = ConfigDict(from_attributes=True)