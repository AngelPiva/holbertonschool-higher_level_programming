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

    for elem in session.query(State).order_by(State.id):
        if elem.name == argv[4]:
            boolean = True
            break
        else:
            boolean = False
    if boolean is True:
        print("{}".format(elem.id))
    else:
        print("Not found")
