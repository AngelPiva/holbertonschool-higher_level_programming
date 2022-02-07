#!/usr/bin/python3
"""
module that create a class Base
"""
import json
import os


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
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

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ is 'Square':
            dummy = cls(2, 2, 2, 2)
        if cls.__name__ is 'Rectangle':
            dummy = cls(2, 2, 2, 2, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        if os.path.isfile(cls.__name__ + '.json') is False:
            return []
        with open(cls.__name__ + '.json', encoding='utf-8') as op:
            list_instances = []
            json_instances = cls.from_json_string(op.read())

            for items in json_instances:
                list_instances.append(cls.create(**items))

            return list_instances
