from sqlalchemy.orm import Mapped, mapped_column
from app.core.models.base import Base

class User(Base):  # Model -> Table
    __tablename__ = "users"    #Имя таблицы.

    id: Mapped[int] = mapped_column(primary_key=True) #Первичный ключ (уникальный идентификатор записи).
    name: Mapped[str] = mapped_column(nullable=False) # Поля, которые нельзя оставить пустыми (опция nullable=False).
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False) #Должно быть уникальным (опция unique=True).

    age: Mapped[int] # Можно не указывать