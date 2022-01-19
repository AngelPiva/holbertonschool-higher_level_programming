#!/usr/bin/python3
"""
class Square
"""
class Square:
    def __init__(self, size=0):
        """
        initializes the data
        """
        self.size = size

    def size(self):
        """
        gets the size value
        """
        return self.__size

    def size(self, value):
        """sets the size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """returns the square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with a character"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for n in range(self.size):
                    print("#", end="")
                print("")
                """sets the size value"""
