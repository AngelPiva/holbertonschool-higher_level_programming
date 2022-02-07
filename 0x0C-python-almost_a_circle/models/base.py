#!/usr/bin/python3
"""
module that create a class Base
"""
import json


class Base:
    """ This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as op:
            json = []
            if list_objs is None:
                return op.write(cls.to_json_string(json))
            for items in list_objs:
                json.append(items.to_dictionary())

            return op.write(cls.to_json_string(json))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)
