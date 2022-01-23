#!/usr/bin/python3
""" module to add two numbers 
a and b can be integers or floats
"""
def add_integer(a, b=98):
    """ funtion that adds two integeres and return the sum """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
