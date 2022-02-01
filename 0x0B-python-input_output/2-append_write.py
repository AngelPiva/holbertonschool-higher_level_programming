#!/usr/bin/python3
"""
module
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
    returns:
            number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as app:
        return app.write(text)
