#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for i in name[0:]:
        if i[0] == '_':
            continue
        else:
            print(i)
