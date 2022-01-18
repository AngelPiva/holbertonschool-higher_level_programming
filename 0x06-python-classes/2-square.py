#!/usr/bin/python3
"""
class square
"""


class Square:
    """description
    class that defines square
    """
    def __init__(self, size=0):
        """size >= 0 and size is int"""
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
