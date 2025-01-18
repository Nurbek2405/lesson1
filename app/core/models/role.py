from app.core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Role(Base):
    __tablename__ = 'roles'

    title: Mapped[str] = mapped_column(nullable=False, unique=True)



# admin
# user
# guest
# moderator