#!/usr/bin/python3
"""
class square
"""


class Square:
    """description
    class that defines square
    """
    def __init__(self, size=0):
        """initializes the datawith conditions"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """square area"""
        return self.__size * self.__size
