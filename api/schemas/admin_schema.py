from pydantic import BaseModel

class AdminBase(BaseModel):
    name: str
    email: str
    password: str

class AdminCreate(AdminBase):
    pass

class AdminSchema(AdminBase):
    admin_id: int

    class Config:
        from_attributes = True