#!/usr/bin/python3
"""
module that defines a class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inhertits from (7-base_geometry.py) """
    def __init__(self, width, height):
        """ initializes the data """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def __str__(self):
        """ returns a rectangle description """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
