#!/usr/bin/python3
"""
module that inherits from list
"""


class MyList(list):
    """ class that that inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
