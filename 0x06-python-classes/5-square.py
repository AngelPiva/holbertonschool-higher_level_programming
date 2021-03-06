#!/usr/bin/python3
"""
class Square
"""


class Square:
    """defines a class square"""
    def __init__(self, size=0):
        """
        initializes the data
        """
        self.size = size

    @property
    def size(self):
        """gets the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with a character"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print("")
                """sets the size value"""
