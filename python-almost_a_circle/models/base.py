#!/usr/bin/python3
"""

Class Base

"""


import json


class Base:
    """
    Class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file """
        # Filename will be <Class name>.json
        filename = cls.__name__ + ".json"
        if list_objs:
            list_d = []
            for obj in list_objs:
                # Append dict representation of obj
                list_d.append(obj.to_dictionary())
            # Convert the list of dict to json string
            j_str = cls.to_json_string(list_d)
        else:
            j_str = "[]"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls(7, 7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_inst = []

        try:
            with open(filename, "r", encoding="utf-8") as f:
                inst = cls.from_json_string(f.read())
                for elem in inst:
                    list_inst.append(cls.create(**elem))
        except FileNotFoundError:
            return list_inst

        return list_inst
