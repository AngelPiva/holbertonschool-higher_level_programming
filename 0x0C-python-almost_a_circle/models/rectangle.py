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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, height):
        """ to set it """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ retrieves x """
        return self.__x

    @x.setter
    def x(self, x):
        """ to set it """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ retrieves y """
        return self.__y

    @y.setter
    def y(self, y):
        """ to set it """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance """
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
