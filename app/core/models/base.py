from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): #Позволяет создавать классы, которые будут отображаться на таблицы в базе данных.
    __abstract__ = True                     # Все модели (классы) должны наследоваться от этого класса.
