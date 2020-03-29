#!/usr/bin/python3
''' Print State '''

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id).filter(State.name == sys.argv[4])

    if (result.first() is None):
        print("Not found")
    else:
        print(result[0][0])
