#!/usr/bin/python3
"""
script that lists all State objects from a database
"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_obj = State(name="Louisiana")
    session.begin()
    session.add(new_obj)
    session.commit()
    print("{}".format(new_obj.id))
