from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column #, relationship
from app.core.models.base import Base

class Todo(Base):
    # id
    name: Mapped[str]
    description: Mapped[str]
    #user: Mapped[List["Parent"]] = relationship(back_populates="todos")
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))





