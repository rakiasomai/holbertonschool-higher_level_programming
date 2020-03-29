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
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states\
            ON cities.state_id=states.id\
            ORDER BY cities.id ASC')
    allStates = cur.fetchall()

    for city in allStates:
        print(city)

    cur.close()
    datab.close()
