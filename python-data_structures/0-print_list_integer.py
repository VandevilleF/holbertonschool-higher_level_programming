#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list

    Parameters:
    - my_list (lists): List from which integers are printed

    Returns:
    int: Integers of the list, one per line

    """
    for i in my_list:
        print("{:d}".format(i))
