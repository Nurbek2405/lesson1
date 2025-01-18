from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database.helper import get_session

from app.core.repos.user import UserRepository
from app.core.services.user import UserService


def get_user_service(session: Annotated[Session, Depends(get_session)]) -> UserService:
    repo = UserRepository(session)
    return UserService(repo)