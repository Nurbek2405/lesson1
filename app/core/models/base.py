from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase): #Позволяет создавать классы, которые будут отображаться на таблицы в базе данных.
    __abstract__ = True                     # Все модели (классы) должны наследоваться от этого класса.

    id: Mapped[int] = mapped_column(primary_key=True) #Первичный ключ (уникальный идентификатор записи).