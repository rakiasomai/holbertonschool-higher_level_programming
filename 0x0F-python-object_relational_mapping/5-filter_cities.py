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
    Take = """SELECT cities.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         WHERE states.name=%s
         ORDER BY cities.id ASC"""
    cur.execute(Take, (sys.argv[4],))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))

    cur.close()
    datab.close()
