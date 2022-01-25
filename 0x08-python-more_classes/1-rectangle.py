#!/usr/bin/python3
"""
module that create a class Rectangle
"""


class Rectangle:
    """
    class Rectangule
    """
    def __init__(self, width=0, height=0):
        """ initializes the data """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width data"""
        return self.__width

    @width.setter
    def width(self, value):
        """ to set width data """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the width data """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set the height data """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
