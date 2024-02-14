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

    def to_json(self):
        if hasattr(self, '__dict__'):
            obj_dict = self.__dict__

        json_dict = {}

        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value

        return json_dict
