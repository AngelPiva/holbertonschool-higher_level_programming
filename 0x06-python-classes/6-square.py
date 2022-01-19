#!/usr/bin/python3
"""
class Square
"""


class Square:
    """
    class that defines a class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the data"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position value"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square"""
        if self.__position[1] <= 0:
            print("", end="")
        else:
            for z in range(self.__position[1]):
                print("")

        if self.__size == 0:
            print("")
        else:
            for n in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
