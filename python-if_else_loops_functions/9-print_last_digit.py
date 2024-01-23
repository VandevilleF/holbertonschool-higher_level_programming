#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number

    Parameters:
    - number (int): Number whose the last digitmust be returned

    Returns:
    int: Value of the last digit

    """
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit
