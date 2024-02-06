#!/usr/bin/python3
"""divides all elements of a matrix
matrix must be a list of lists of integers or floats
Each row of the matrix must be of the same size
div must be a number (int or float), div can't be equal to 0
Elements of matrix be divided by div, rounded to 2 decimal"""
def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by div
    """

    mat_err = ("matrix must be a matrix (list of lists) of integers/floats")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(mat_err)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_div = [[0] * len(row) for row in matrix]

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError ("Each row of the matrix must have the same size")

    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            matrix_div[i][j] = round((matrix[i][j] / div), 2)
            
    return matrix_div
