from sqlalchemy import Column, Integer, String, DateTime

from app.db.base import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birthday = Column(DateTime)
    work_quality = Column(Integer)
    password = Column(String)
    comment = Column(String)
    comment2 = Column(String)

    def to_dict(self):
        return {"name": self.name, "birthday": self.birthday, "work_quality": self.work_quality, "password": self.password}

    def __str__(self):
        return f"Пользователь с номером {self.id} по имени {self.name} с паролем {self.password}."
