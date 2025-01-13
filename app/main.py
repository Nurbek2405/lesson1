from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
)
from fastapi import FastAPI
from app.core.models.base import Base

class User(Base):  # Model -> Table
    __tablename__ = "users"    #Имя таблицы.

    id: Mapped[int] = mapped_column(primary_key=True) #Первичный ключ (уникальный идентификатор записи).
    name: Mapped[str] = mapped_column(nullable=False) # Поля, которые нельзя оставить пустыми (опция nullable=False).
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False) #Должно быть уникальным (опция unique=True).

    age: Mapped[int]

# Создание движка
engine = create_engine(
    url="postgresql://postgres:postgres@localhost:6432/test",
    echo=True, # Включает логирование SQL-запросов.
)
SessionLocal = sessionmaker(bind=engine)    #Создает фабрику для сессий, привязывая их к engine.
session = SessionLocal                      #Сессии используются для выполнения запросов к базе данных.

# Создание всех таблиц ( если будет писать not exist, то что не создана)
#Base.metadata.create_all(bind=engine) #Создает таблицы в базе данных на основе всех определенных моделей (User в данном случае).
                                        #Использует метаданные (Base.metadata) для создания SQL-запросов CREATE TABLE.
# INSERT Вставка данных
try:
    with SessionLocal() as session:  # INSERT INTO users (name, password, email, age) VALUES (...);
        query = insert(User).values( #Создается запрос INSERT для вставки данных в таблицу users.
            name="User3",
            password="user3",
            email="user3@gmail.com",
            age=23,
        )
        result = session.execute(query)  # Исправлено Исполняет SQL-запрос.
        session.commit()
        # for user in result.scalars():
        #     print(user.name, user.email)

        #print(f"Данные успешно добавлены: {result.rowcount} строк(и).")
        # print(result.all()) # print(dir(result))
        #print(result.scalar())  #scalar  scalar_one_or_none   #Данные успешно добавлены: 1 строк(и). None

        # user = User()
        # session.add(user)
        # session.commit()
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()

#UPDATE
try:
    with SessionLocal() as session:
        query = update(User).filter_by(id=9).values(name="User9", password="User9")
    result = session.execute(query)
    session.commit()
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()


#SELECT
try:
    with SessionLocal() as session:
        query = select(User).filter_by(id=1)
    result = session.execute(query)
    session.commit()
    for user in result.scalars():
        print(user.name, user.email)
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()

#DELETE
try:
    with SessionLocal() as session:
        query = delete(User).filter_by(id=2)
    result = session.execute(query)
    # query = delete(User).where(User.id == 2)
    session.commit()
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()

app = FastAPI()

def get(model, **kwargs):
    with SessionLocal() as session:
        query = select(model).filter_by(**kwargs) # filter_by(id=6)

        result = session.execute(query)
        session.commit()

        return result.scalar_one_or_none()

def get_all(model):
    with SessionLocal() as session:
        query = select(User.id)

        result = session.execute(query)
        session.commit()

        return result.fetchall()

@app.get("/one")
def get_user():
    return get(model=User, id=6)

@app.get("/all")
def get_user():
    return get_all(model=User)


# SQL Query
# SELECT * FROM user;
# INSERT
# UPDATE
# DELETE

# *args, **kwargs
# filter_by
# where
# def remove(model, **kwargs):
#     with SessionLocal() as session:
#         query = delete(User).filter_by(**kwargs)
#         result = session.execute(query)
#     # query = delete(User).where(User.id == 2)
#         session.commit()

# def alter():
#     pass

#users = get(model=User, id=7)
# remove(model=User, id=7)



        # for user in result:
        #     print(user.name)

        #return result

# class Admin(Base):
#     pass




# admins = get(model=Admin)



# def function(number,text, *args , **kwargs):
#     #print(number,text)
#     print(kwargs) # в словарь закидывает получается если есть атрибуты присовенные
#     #print(args) # в словарь закидывает получается
#
# function(number=3, text="swqfqwf", age=13, last_name="python", n=253, u=True)
# #function(3, "swqfqwf", 13,"python", 253, True)
