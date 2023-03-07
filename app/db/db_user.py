from app.db.base_db import DbBase
from app.db.models import User


class DbUsers(DbBase):
    data_model = User


db_users = DbUsers()
