#!/usr/bin/python3
"""
module
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    returns:
            the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as w:
        return w.write(text)
