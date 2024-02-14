#!/usr/bin/python3
"""

A class Student that defines

"""


class Student:
    """
    A class Student that defines
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dict_attr = {}
            for at in attrs:
                if type(at) is str:
                    if hasattr(self, at):
                        dict_attr[at] = getattr(self, at)
            return dict_attr

        return self.__dict__
