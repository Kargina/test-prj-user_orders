from user_project.db import Base, User, Orders
from user_project.db import Session
from sqlalchemy.engine import create_engine
from user_project.config import DB_PATH

def seed_data(session):
    

    Base.metadata.create_all(engine)
    
    u1 = User(name='Ivan Petrov', department='Development')
    session.add(u1)
    u2 = User(name='Pert Ivanov', department='QA')
    session.add(u2)
    u3 = User(name='Jim Beam', department='Office')
    session.add(u3)
    o1 = Orders(user_id=1, text='add more fruit', date='01.01.20')
    session.add(o1)
    o2 = Orders(user_id=1, text='new keyboard', date='02.01.20')
    session.add(o2)
    o3 = Orders(user_id=2, text='fix a kitchen sink', date='03.01.20')
    session.add(o3)
    o4 = Orders(user_id=2, text='business trip to Moscow', date='04.01.20')
    session.add(o4)

    session.commit()


if __name__ == '__main__':
    engine = create_engine(f"sqlite:///{DB_PATH}")
    Session.configure(bind=engine)
    seed_data(Session())
