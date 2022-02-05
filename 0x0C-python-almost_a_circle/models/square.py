#!/usr/bin/python3
"""
module that defines a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square  that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor: initializes the data """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns "[Square] (<id>) <x>/<y> - <size>"
        - in our case, width or height
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ to retrieve it """
        return self.width

    @size.setter
    def size(self, size):
        """ to set it """
        self.__width = size
        self.__height = size
