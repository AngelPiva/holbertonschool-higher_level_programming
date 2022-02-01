#!/usr/bin/python3
"""
module
"""


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ initializes the data """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        attr_cont = {}
        if type(attrs) is list:
            for elem in attrs:
                if type(elem) is not str:
                    return self.__dict__
                if elem in self.__dict__:
                    attr_cont[elem] = self.__dict__[elem]
            return attr_cont
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for n in json:
            self.__dict__[n] = json[n]
