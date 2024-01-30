#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    """
    Replaces or adds key/value in a dictionary

    Parameters:
    - a_dictionary (dict): Actual dictonary
    - key (str): Key in dictonary, will be always a string
    - value (): Value of key, will be any type

    Returns:
    dict: Dictionary with key/value added or replaced

    """
    a_dictionary[key] = value

    return a_dictionary
