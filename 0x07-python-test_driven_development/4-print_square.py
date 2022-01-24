#!/usr/bin/python3
"""
module that prints a square with size size
"""


def print_square(size):
    """ function that prints a square with size size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        for i in range(size):
            print("#", end="")
        print("")
