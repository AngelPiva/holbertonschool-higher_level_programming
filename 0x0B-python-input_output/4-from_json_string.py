#!/usr/bin/python3
"""
module
"""
import json


def from_json_string(my_str):
    """ returns an object (Python data struct) represented by a JSON string """
    return json.loads(my_str)
