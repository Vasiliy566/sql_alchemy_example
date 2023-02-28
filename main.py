from datetime import datetime

from db.base import Session
from db.models import User


def add_user(name: str, birthday: datetime, work_quality: int, password: str) -> None:
    user = User(name=name, birthday=birthday, work_quality=work_quality, password=password)
    session = Session()
    session.add(user)
    session.commit()
    session.close()


def get_user(user_id: int) -> User | None:
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user


def delete_user(user_id: int):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.delete(user)
    session.commit()
    session.close()


def change_password(user_id: int, new_password: str) -> User:
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    user.password = new_password
    session.add(user)
    session.commit()
    session.close()
    return get_user(user_id)


u = get_user(2)
print(u)

change_password(2, "123456")
u = get_user(2)
print(u)

