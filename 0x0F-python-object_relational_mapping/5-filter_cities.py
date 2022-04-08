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
    cursor.execute("SELECT cities.name, cities.id \
                    FROM cities \
                    JOIN states \
                    ON states.id = cities.state_id \
                    WHERE states.name LIKE '{}' \
                    ORDER BY cities.id ASC;".format(argv[4]))
    elems = cursor.fetchall()

    if elems is not None:
        for elem in range(len(elems)):
            if elem != len(elems) - 1:
                print(f'{elems[elem][0]}, ', end="")
            else:
                print(f'{elems[elem][0]}', end="")
        print("")
    con_datab.close()
