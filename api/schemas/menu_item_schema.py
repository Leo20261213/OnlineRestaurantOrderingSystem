from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    category: str | None = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemSchema(MenuItemBase):
    item_id: int

    class Config:
        from_attributes = True