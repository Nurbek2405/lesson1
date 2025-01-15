from typing import Annotated
from fastapi import APIRouter, Depends

from app.core.services.user import UserService
from app.core.schemas.user import UserCreate, UserRead, UserUpdate

from app.api.depends.user import get_user_service

router = APIRouter(prefix="/api/user", tags=["Users"])


@router.get("/", response_model=list[UserRead])
def get_all(service: Annotated[UserService, Depends(get_user_service)]):
    return service.get_all()


@router.get("/{id}", response_model=UserRead)
def get_one_by_id(id: int, service: Annotated[UserService, Depends(get_user_service)]):
    return service.get_one(id=id)


@router.post("/", response_model=UserRead)
def create(
    data: UserCreate,
    service: Annotated[UserService, Depends(get_user_service)],
):
    return service.create(data)


@router.patch("/{id}", response_model=UserRead)
def update(
    id: int,
    data: UserUpdate,
    service: Annotated[UserService, Depends(get_user_service)],
):
    return service.update(data, id=id)


@router.delete("/{id}", status_code=204)
def delete(
    id: int,
    service: Annotated[UserService, Depends(get_user_service)],
):
    return service.delete(id=id)