#!/usr/bin/python3
"""

class MyList that inherits from list

"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        for element in self:
            if type(element) is not int:
                raise TypeError("all the elements of the list will be int")
        print(sorted(self))
