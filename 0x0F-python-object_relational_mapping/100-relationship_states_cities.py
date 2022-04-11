#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """ to make sure that code isn´t
    going to be executed when imported """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
