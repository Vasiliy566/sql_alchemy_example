from datetime import datetime

import alembic
import pytest
from alembic.config import Config

from app.db.base import get_session
from app.db.db_user import DbUsers
from testcontainers.postgres import PostgresContainer
import sqlalchemy


DATE = datetime.strptime('01/01/22', '%m/%d/%y')


@pytest.fixture
def db():
    return DbUsers(get_session)


@pytest.fixture
def test_db():
    with PostgresContainer("postgres:14.7") as postgres:
        engine = sqlalchemy.create_engine(postgres.get_connection_url())
        config = Config("alembic.ini")
        alembic.command.upgrade(config, "head")
        return engine
        # engine = sqlalchemy.create_engine(postgres.get_connection_url())


def test_add(db):
    data = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}

    db.add(data)

    u = db.get({"name": "Vasya"})
    assert u.to_dict() == data
    db.delete({"name": "Vasya"})


def test_get(db):
    data = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}

    db.add(data)

    u = db.get({"name": "Vasya"})
    assert u.to_dict() == data
    db.delete({"name": "Vasya"})


def test_update(db):
    d = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}
    u = db.add(d)

    u = db.update({"id": u.id}, {"name": "Petya"})
    assert u.to_dict() == {"name": "Petya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}
    db.delete({"name": "Petya"})


def test_delete(db):
    data = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}

    db.add(data)
    db.delete({"name": "Vasya"})

    u = db.get({"name": "Vasya"})
    assert u is None
