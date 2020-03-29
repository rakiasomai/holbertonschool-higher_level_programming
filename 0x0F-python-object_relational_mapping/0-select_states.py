#!/usr/bin/python3
''' List all states from a given datab sorted in ascending order by id '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    datab = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = datab.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    datab.close()
