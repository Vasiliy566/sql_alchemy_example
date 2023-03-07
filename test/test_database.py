from datetime import datetime

from app.db.db_user import DbUsers

DATE = datetime.strptime('01/01/22', '%m/%d/%y')


def test_add():
    data = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}

    db = DbUsers()
    db.add(data)

    u = db.get({"name": "Vasya"})
    assert u.to_dict() == data
    db.delete({"name": "Vasya"})


def test_get():
    data = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}

    db = DbUsers()
    db.add(data)

    u = db.get({"name": "Vasya"})
    assert u.to_dict() == data
    db.delete({"name": "Vasya"})


def test_update():
    db = DbUsers()
    d = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}
    u = db.add(d)

    u = db.update({"id": u.id}, {"name": "Petya"})
    assert u.to_dict() == {"name": "Petya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}
    db.delete({"name": "Petya"})


def test_delete():
    data = {"name": "Vasya", "birthday": DATE, "work_quality": 0, "password": "Vasya1"}

    db = DbUsers()
    db.add(data)
    db.delete({"name": "Vasya"})

    u = db.get({"name": "Vasya"})
    assert u is None
