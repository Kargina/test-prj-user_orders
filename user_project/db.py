from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User, backref="orders")

    text = Column(String)
    date = Column(String)


Session = sessionmaker()


def user_list():
    return Session().query(User)


def count_user_orders(user_id):
    return Session().query(Orders).filter(Orders.user_id == user_id).count()


def user_orders(user_id):
    return Session().query(Orders).filter(Orders.user_id == user_id)


def get_user_by_id(user_id):
    return Session().query(User).get(user_id)
