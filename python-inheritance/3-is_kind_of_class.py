#!/usr/bin/python3
"""
returns True if the object is an instance of
or if the object is an instance of a class that inherited from
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is instance of, or object of a class
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
