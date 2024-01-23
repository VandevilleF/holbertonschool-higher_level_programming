#!/usr/bin/python3
def fizzbuzz():
    """
    Computes a to the power of b and return the value.

    Parameters:
    - a (int): First integer to compute
    - b (int): Seconde integer to compute

    Returns:
    int: the value of a to the power of b

    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{}".format(i), end=' ')
