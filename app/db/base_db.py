from app.db.base import get_session


class DbBase:
    data_model = None

    def add(self, data: dict):
        with get_session() as session:
            to_add = self.data_model(**data)
            session.add(to_add)
            session.commit()
            session.refresh(to_add)
            return to_add

    def get(self, filtered_by: dict):
        with get_session() as session:
            return session.query(self.data_model).filter_by(**filtered_by).first()

    def delete(self, filtered_by: dict):
        with get_session() as session:
            to_delete = session.query(self.data_model).filter_by(**filtered_by).first()
            session.delete(to_delete)
            session.commit()

    def update(self, filtered_by: dict, data: dict):
        with get_session() as session:
            to_update = session.query(self.data_model).filter_by(**filtered_by).first()
            new_data = to_update.to_dict()
            new_data.update(data)

            new_model = self.data_model(**new_data)
            session.add(new_model)
            session.commit()
            session.refresh(new_model)
            return new_model

