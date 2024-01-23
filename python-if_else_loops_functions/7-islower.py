#!/usr/bin/python3
def islower(c):
    """
    Checks for lowercase character

    Parameters:
    - c (chr): character to check

    Returns:
    bool: True if c is lowercase, False otherwise

    """
    if ord(c) in range(97, 123):
        return True
    else:
        return False
