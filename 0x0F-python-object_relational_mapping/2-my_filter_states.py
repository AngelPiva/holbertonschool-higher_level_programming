#!/usr/bin/python3
"""
module that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ to make sure that code isn´t
    going to be executed when imported """
    con_datab = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], port=3306, database=argv[3])
    cursor = con_datab.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE '{}' \
                    ORDER BY states.id ASC;".format(argv[4]))
    elems = cursor.fetchall()

    for elem in elems:
        print(elem)
    con_datab.close()
