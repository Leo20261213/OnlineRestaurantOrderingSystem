from pydantic import BaseModel, EmailStr, ConfigDict

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None

    # Updated for Pydantic v2
    model_config = ConfigDict(from_attributes=True)