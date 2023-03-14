from fastapi import Depends

from app.db.db_user import DbUsers
from app.services.get_user_service import GetUser


def db_dependency() -> DbUsers:
    return DbUsers()


def get_user_dependency(
    db=Depends(db_dependency)
) -> GetUser:
    return GetUser(db)
