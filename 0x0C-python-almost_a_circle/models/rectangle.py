#!/usr/bin/python3
"""
module that defines a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor: initializes the data """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieves width """
        return self.__width

    @width.setter
    def width(self, width):
        """ to set it """
        self.__width = width

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, height):
        """ to set it """
        self.__height = height

    @property
    def x(self):
        """ retrieves x """
        return self.__x

    @x.setter
    def x(self, x):
        """ to set it """
        self.__x = x

    @property
    def y(self):
        """ retrieves y """
        return self.__y

    @y.setter
    def y(self, y):
        """ to set it """
        self.__y = y
