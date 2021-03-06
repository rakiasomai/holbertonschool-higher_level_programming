#!/usr/bin/python3
''' Print all STATES '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    datab = MySQLdb.connect(user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3],
                            host='localhost',
                            port=3306)
    cur = datab.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    StatesN = cur.fetchall()

    for state in StatesN:
        if (state[1][0] == 'N'):
            print(state)
    cur.close()
    datab.close()
