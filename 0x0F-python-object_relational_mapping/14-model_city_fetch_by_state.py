#!/usr/bin/python3
''' print all cities '''

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for k in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(k.State.name, k.City.id, k.City.name))
