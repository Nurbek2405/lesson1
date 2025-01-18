from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import datetime, timezone
from sqlalchemy import DateTime
class Base(DeclarativeBase): #Позволяет создавать классы, которые будут отображаться на таблицы в базе данных.
    __abstract__ = True                     # Все модели (классы) должны наследоваться от этого класса.

    id: Mapped[int] = mapped_column(primary_key=True) #Первичный ключ (уникальный идентификатор записи).

    created_at: Mapped[datetime] = mapped_column( # когда было создана запись
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))

    updated_at: Mapped[datetime] = mapped_column(  # когда была обновлена запись
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))