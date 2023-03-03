from datetime import datetime

from db.base import Session, get_session
from db.base_db import DbBase
from db.models import User


# def add_user(session: Session, name: str, birthday: datetime, work_quality: int, password: str) -> None:
#     user = User(name=name, birthday=birthday, work_quality=work_quality, password=password)
#     session.add(user)
#     session.commit()
#
#
# def get_user(session: Session, user_id: int) -> User | None:
#     return session.query(User).filter_by(id=user_id).first()
#
#
# def delete_user(session: Session, user_id: int) -> None:
#     user = session.query(User).filter_by(id=user_id).first()
#     session.delete(user)
#     session.commit()
#
#
# def change_password(session: Session, user_id: int, new_password: str) -> User:
#     user = session.query(User).filter_by(id=user_id).first()
#     user.password = new_password
#     session.add(user)
#     session.commit()
#     return get_user(session, user_id)


class DbUsers(DbBase):
    data_model = User

    def add(self, data: dict):
        with get_session() as session:
            to_add = self.data_model(**data)
            session.add(to_add)
            session.commit()

    def get(self, filtered_by: dict):
        with get_session() as session:
            return session.query(self.data_model).filter_by(**filtered_by).first()

    def delete(self):
        raise NotImplemented

    def update(self):
        raise NotImplemented


if __name__ == "__main__":
    db = DbUsers()
    d = {"name": "Vasya", "birthday": datetime.now(), "work_quality": 0, "password": "Vasya1"}
    db.add(d)

    u = db.get({"name": "Vasya"})
    print(u.id)

    u = db.get({"work_quality": "0"})
    print(u.id)

    u = db.get({"password": "Vasya1"})
    print(u.id)
