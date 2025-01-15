from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    url=str(settings.db.url),
    echo=settings.db.echo,
)


SessionLocal = sessionmaker(bind=engine)


def get_session():
    with SessionLocal() as session:
        yield session