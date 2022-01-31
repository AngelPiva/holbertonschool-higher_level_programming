#!/usr/bin/python3
"""
module Only sub class of
"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited """
    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is False:
            return True
    return False
