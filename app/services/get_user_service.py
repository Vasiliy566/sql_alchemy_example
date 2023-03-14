from app.db.db_user import DbUsers


class GetUser:
    def __init__(self, db: DbUsers):
        self.db_ = db

    def __call__(self, user_id):
        return self.db_.get({"id": user_id})
