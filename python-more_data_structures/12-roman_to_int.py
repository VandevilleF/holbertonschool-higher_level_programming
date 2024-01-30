#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0

    # Creat dictionary with Roman num
    rom_int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    value = 0
    prev = 0
    for r in roman_string:
        # If prev num is lower than actual num
        # Substract twice the prev value from the actual value
        # The subtraction is necessary because the previous value
        # was added in the previous iteration, and it needs
        # to be subtracted to correct the total
        if prev < rom_int.get(r):
            value += (rom_int.get(r) - 2 * prev)
        else:
            # Add value of actual num to the total
            value += rom_int.get(r)
        # Update the previous value for the next iteration.
        prev = rom_int.get(r)

    return value
