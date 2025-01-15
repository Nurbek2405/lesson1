from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.models.base import Base
from app.core.models.user import User
from app.core.models.role import Role
from app.core.database.helper import engine

from app.api.api_v1.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    #Start up
    # Создание всех таблиц ( если будет писать not exist, то что не создана)
    # Создает таблицы в базе данных на основе всех определенных моделей (User в данном случае).
    # Использует метаданные (Base.metadata) для создания SQL-запросов CREATE TABLE.
    #Base.metadata.drop_all(bind=engine) # удалить все таблицы
    Base.metadata.create_all(bind=engine) # создаем все таблицы, всегда держалась чистой
    print('Starting.... lifespan')
    yield
    print('Shutting down.... lifespan')
    #Base.metadata.drop_all(bind=engine) # удалить все таблицы
app = FastAPI(lifespan=lifespan)
app.include_router(user_router)


# @app.get("/one") # endpoinds api
# def get_user():
#     return get(model=User, id=6)
#
# @app.get("/all")
# def get_user():
#     return get_all(model=User)


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
