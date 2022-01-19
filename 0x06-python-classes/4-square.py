#!/usr/bin/python3
"""
class square
"""


class Square():
    """
    class that defines Square
    """
    def __init__(self, size=0):
        """initializes the data"""
        self.size = size

    @property
    def size(self):
        """to get the size of the square"""
        return self.__size

    def area(self):
        """returns square area"""
        return self.size * self.size
    
    @size.setter
    def size(self, value):
        """to set the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
