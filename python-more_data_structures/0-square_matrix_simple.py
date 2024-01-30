#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[0] * len(row) for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_square[i][j] = pow(matrix[i][j], 2)

    return matrix_square
