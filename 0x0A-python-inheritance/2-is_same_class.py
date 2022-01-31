#!/usr/bin/python3
"""
module that checks for an instance in a specified class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is an instance of the specified class """
    if type(obj) == a_class:
        return True
    return False
