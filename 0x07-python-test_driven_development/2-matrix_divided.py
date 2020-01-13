#!/usr/bin/python3
'''
This is a function called "matrix_divided"
This function can takes a list of lists matrix & divisor.
All elements are divided by the divisor & returned new matrix.
'''


def matrix_divided(matrix, div):
    '''
    Return a new matrix with all values divided by the divisor
    '''
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(y) > 0 for y in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(y) == len(matrix[0]) for y in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for y in matrix:
        if not isinstance(y, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(isinstance(z, (int, float)) for z in y):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for y in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), y)))

    return new_matrix
