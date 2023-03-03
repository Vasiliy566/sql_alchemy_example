from typing import Callable

from db.base import Base, get_session


class DbBase:
    data_model = None
    # def __init__(self, data_model):
    #     self.data_model = data_model

    def add(self, data: dict):
        with get_session() as session:
            to_add = self.data_model(**data)
            session.add(to_add)
            session.commit()

    def get(self, filtered_by: dict):
        with get_session() as session:
            return session.query(self.data_model).filter_by(**filtered_by).first()
