#!/usr/bin/python3
"""
module that defines a class Square
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size):
        """ initializes the data """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
