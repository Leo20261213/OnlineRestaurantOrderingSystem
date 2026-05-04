from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    role: str | None = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True