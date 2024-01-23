#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    if len(argv) == 1:
        print("{}".format(int(0)))
    else:
        for i in argv[1:]:
            result += int(i)
        print("{}".format(int(result)))
