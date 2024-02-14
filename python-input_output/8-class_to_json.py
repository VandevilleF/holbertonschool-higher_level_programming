#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object"""
    if hasattr(obj, '__dict__'):
        obj_dict = obj.__dict__

        json_dict = {}

        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value

        return json_dict
