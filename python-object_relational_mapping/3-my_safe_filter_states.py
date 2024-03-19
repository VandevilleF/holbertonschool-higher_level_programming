#!/usr/bin/python3
"""
takes in arguments and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
But one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()
    query_name = argv[4] + '%'
    query = """SELECT * FROM states WHERE name LIKE BINARY %s
                ORDER BY id ASC"""
    cur.execute(query, (query_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
