#!/usr/bin/python3
''' Print the first State '''

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id, State.name).first()
    if (result is None):
        print("Nothing")
    else:
        print("{:d}: {}".format(result[0], result[1]))
