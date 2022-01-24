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
        self.height = height
        self.width = width

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
            raise TypeError("width must be >= 0")
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
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
