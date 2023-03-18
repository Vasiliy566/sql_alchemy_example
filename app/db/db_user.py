from app.db.base import get_session
from app.db.base_db import DbBase
from app.db.models import User


class DbUsers(DbBase):
    data_model = User


def db_users_fabric():
    return DbUsers(get_session)
