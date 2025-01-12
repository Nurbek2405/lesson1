from pydantic import BaseModel, EmailStr

# create, update, read (get)


class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr

