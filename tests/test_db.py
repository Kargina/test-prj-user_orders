import pytest
from sqlalchemy.engine import create_engine
from user_project.db import Session, User, get_user_by_id, Base


def test_get_user():

    engine = create_engine("sqlite://")
    Session.configure(bind=engine)
    s = Session()
    Base.metadata.create_all(engine)
    u1 = User(name='Ivan Petrov', department='Development')
    s.add(u1)
    s.commit()
    ivan = get_user_by_id(1)

    assert ivan.name == "Ivan Petrov"