from typing import Optional
from pydantic import BaseModel, EmailStr
# Схема Pydantic
# create, update, read (get)


class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr # user@gmail.com
    age: Optional[int] = None # Опциональные это не обязательно

class UserRead(BaseModel):
    id: int
    name: str
    password: str
    email: EmailStr # user@gmail.com
    age: Optional[int] = None # Опциональные это не обязательно

class UserUpdate(BaseModel):
    name: Optional[str] = None # обновляется одно только меняется
    password: Optional[str] = None
    email: Optional[EmailStr] = None # user@gmail.com
    age: Optional[int] = None # Опциональные это не обязательно
