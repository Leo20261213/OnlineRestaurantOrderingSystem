from pydantic import BaseModel

class RestaurantStaffBase(BaseModel):
    name: str
    role: str
    email: str

class RestaurantStaffCreate(RestaurantStaffBase):
    pass

class RestaurantStaffSchema(RestaurantStaffBase):
    staff_id: int

    class Config:
        from_attributes = True