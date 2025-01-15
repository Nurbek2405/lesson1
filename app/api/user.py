from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.database.helper import get_session

from sqlalchemy import select,insert, update, delete

from app.core.models.user import User

from sqlalchemy.orm import Session

from app.core.schemas.user import UserCreate, UserUpdate, UserRead
router = APIRouter(prefix="/api/user", tags=["Группа, USERS access 2"]) # с тегами будет разделение, лучше

@router.get("/", response_model=list[UserRead])
def get_all(session: Annotated[Session, Depends(get_session)]):
    query = select(User)
    result = session.execute(query)
    session.commit()

    return result.scalars().all()

@router.get("/{id}", response_model=UserRead) # для получение
def get_one_by_id(id: int, session: Annotated[Session, Depends(get_session)]):
    query = (select(User)
             .filter_by(id=id)) # filter_by(id=6)
    result = session.execute(query)
    session.commit()

    return result.scalar_one_or_none()

@router.post("/", response_model=UserRead)   # для создание
def create(data: UserCreate, session: Annotated[Session, Depends(get_session)]):
    data_dict: dict = data.model_dump()
    query = (insert(User)
             .values(**data_dict)
             .returning(User)) # returning возвращает insert запрос
    result = session.execute(query)  # Исправлено Исполняет SQL-запрос.
    session.commit()
    return result.scalar_one_or_none()

@router.patch("/{id}", response_model=UserRead)# для обновление
def alter(
        id:int,
        data: UserUpdate,
        session: Annotated[Session, Depends(get_session)]
):
    data_dict: dict = data.model_dump(exclude_unset=True, exclude_none=True)
    query = update(User).filter_by(id=id).values(**data_dict).returning(User)

    result = session.execute(query)
    session.commit()
    return result.scalar_one_or_none()


@router.delete("/{id}")
def remove(
    id: int,
    session: Annotated[Session, Depends(get_session)],
):
    query = delete(User).filter_by(id = id)

    session.execute(query)
    session.commit()
    return f"User: {id} is has been removed!"

# @router.delete("/")
# def remove(
#     ids: list[int],
#     session: Annotated[Session, Depends(get_session)],
# ):
#     query = delete(User).filter_by(id = id)
#
#     session.execute(query)
#     session.commit()
#     return f"User: {id} is has been removed!"




# def get(model, **kwargs):
#     with SessionLocal() as session:
#         query = select(model).filter_by(**kwargs) # filter_by(id=6)
#
#         result = session.execute(query)
#         session.commit()
#
#         return result.scalar_one_or_none()
#
# def get_all(model):
#     with SessionLocal() as session:
#         query = select(User.id)
#
#         result = session.execute(query)
#         session.commit()
#
#         return result.fetchall()




# INSERT Вставка данных
# try:
#     with SessionLocal() as session:  # INSERT INTO users (name, password, email, age) VALUES (...);
#         query = insert(User).values( #Создается запрос INSERT для вставки данных в таблицу users.
#             name="User3",
#             password="user3",
#             email="user3@gmail.com",
#             age=23,
#         )
#         result = session.execute(query)  # Исправлено Исполняет SQL-запрос.
#         session.commit()
#         # for user in result.scalars():
#         #     print(user.name, user.email)
#
#         #print(f"Данные успешно добавлены: {result.rowcount} строк(и).")
#         # print(result.all()) # print(dir(result))
#         #print(result.scalar())  #scalar  scalar_one_or_none   #Данные успешно добавлены: 1 строк(и). None
#
#         # user = User()
#         # session.add(user)
#         # session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
# finally:
#     session.close()

#UPDATE
# try:
#     with SessionLocal() as session:
#         query = update(User).filter_by(id=9).values(name="User9", password="User9")
#     result = session.execute(query)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
# finally:
#     session.close()


#SELECT
# try:
#     with SessionLocal() as session:
#         query = select(User).filter_by(id=1)
#     result = session.execute(query)
#     session.commit()
#     for user in result.scalars():
#         print(user.name, user.email)
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
# finally:
#     session.close()

#DELETE
# try:
#     with SessionLocal() as session:
#         query = delete(User).filter_by(id=2)
#     result = session.execute(query)
#     # query = delete(User).where(User.id == 2)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
# finally:
#     session.close()