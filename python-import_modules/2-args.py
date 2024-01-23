#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if argv == 0:
        print("{} arguments.".format(len(argv) - 1))
    elif argv == 1:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
        
    for count, i in enumerate(argv[1:]):
        print("{}: {}".format(count + 1, i))
