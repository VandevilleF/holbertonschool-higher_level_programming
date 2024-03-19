#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY '{}%'
                ORDER BY cities.id ASC""".format(argv[4]))
    query_rows = cur.fetchall()

    cities_name = []

    for row in query_rows:
        cities_name.append(row[0])

    res = ", ".join(cities_name)
    print(res)
    cur.close()
    conn.close()
