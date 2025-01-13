from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создание движка
engine = create_engine(
    url="postgresql://postgres:postgres@localhost:6432/test",
    echo=True, # Включает логирование SQL-запросов.
)
SessionLocal = sessionmaker(bind=engine)    #Создает фабрику для сессий, привязывая их к engine.
                                              #Сессии используются для выполнения запросов к базе данных.

def get_session():
    with SessionLocal() as session:
        yield session   # текстовые менеджеры, когда надо получить одну сессию удобном образом, чтобы потом не писать везде
        # держит в озу сессию, и потом удаляет