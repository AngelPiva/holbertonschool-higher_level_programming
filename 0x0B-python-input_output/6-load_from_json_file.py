#!/usr/bin/python3
"""
module
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file” """
    with open(filename, encoding='utf-8') as co:
        return json.loads(co.read())
