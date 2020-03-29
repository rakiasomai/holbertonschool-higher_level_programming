#!/usr/bin/python3
''' Delete state withe name containes 'a' '''

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for statee in session.query(State).filter(State.name.like('%a%')):
        session.delete(statee)
    session.commit()
