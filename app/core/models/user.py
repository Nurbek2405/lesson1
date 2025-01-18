from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models.todo import Todo

class User(Base):  # Model -> Table
    __tablename__ = "users"    #Имя таблицы.

    name: Mapped[str] = mapped_column(nullable=False) # Поля, которые нельзя оставить пустыми (опция nullable=False).
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False) #Должно быть уникальным (опция unique=True).

    age: Mapped[int] # Можно не указывать

    todos: Mapped[List["Todo"]] = relationship() # если не указывает то уходит в бд, остается на уровне ORM

