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
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns attributes """
        attrs = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
