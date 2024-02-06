#!/usr/bin/python3
"""Prints a square with the character #
size is the size length of the square
size must be an integer,
if size is less than 0, raise a ValueError
if size is a float and is less than 0, raise a TypeError"""


def print_square(size):
    """
    Prints a square with the character #
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
