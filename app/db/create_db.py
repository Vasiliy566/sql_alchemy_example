from app.db.base import engine, Base
from app.db.models import User

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, tables=[User.__table__])
