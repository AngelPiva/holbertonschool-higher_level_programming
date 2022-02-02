#!/usr/bin/python3
"""
module
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line
    containing a specific string
    """
    with open(filename, encoding='utf-8') as opr:
        new_text = ""
        for line in opr:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w", encoding="utf-8") as w:
        w.write(new_text)
