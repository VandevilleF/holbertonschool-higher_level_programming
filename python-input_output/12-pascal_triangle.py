#!/usr/bin/python3
"""
"""


def pascal_triangle(n):

    if n <= 0:
        return []

    list_num = [[1]]

    for i in range(1, n):
        line = [1]
        for j in range(len(list_num)):
            if j + 1 < len(list_num):
                line.append(list_num[i - 1][j] + list_num[i - 1][j + 1])
        line.append(1)
        list_num.append(line)
    return list_num
