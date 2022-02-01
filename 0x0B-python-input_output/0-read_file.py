#!/usr/bin/python3
"""
module
"""


def read_file(filename=""):
    """ function that writes a string to a text file
    returns:
            the number of characters written
    """
    with open(filename, encoding='utf-8') as o:
        for line in o:
            print(line, end="")
