#!/usr/bin/python3
"""
module that create a class Rectangle
"""


class Rectangle:
    """
    class Rectangule
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes the data """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __print_rect(self):
        """ returns the rectangle with '#' character """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for n in range(self.__width):
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __str__(self):
        """ returns the string representation """
        return self.__print_rect()

    def __repr__(self):
        """ returns a string repr to be able to recreate a new instance """
        r_width = str(eval("self.width"))
        r_height = str(eval("self.height"))
        r = "Rectangle(" + r_width + ", " + r_height + ")"
        return r

    def __del__(self):
        """ prints Bye rectangle when is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns a new rectanle instance with width == height == size """
        return cls(size, size)
