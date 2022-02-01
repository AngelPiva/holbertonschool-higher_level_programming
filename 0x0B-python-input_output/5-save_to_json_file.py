#!/usr/bin/python3
"""
module
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w', encoding="utf-8") as wo:
        wo.write(json.dumps(my_obj))
