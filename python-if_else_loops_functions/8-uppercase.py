#!/usr/bin/env python3
def uppercase(str):
    """
    Prints a string in uppercase

    Parameters:
    - str (str): character to check

    Returns:
    str: A string in uppercase

    """
    
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
            
        print("{}".format(c), end='')
    print("")
    