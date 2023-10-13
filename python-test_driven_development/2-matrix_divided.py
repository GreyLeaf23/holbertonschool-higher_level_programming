#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)

    elif len(matrix) == 0:
        raise TypeError(msg)

    elif not isinstance(matrix[0], list):
        raise TypeError(msg)

    elif len(matrix[0]) == 0:
        raise TypeError(msg)

    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    else:
        new_matrix = []
        for row in matrix:
            new_row = []
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(msg)
                else:
                    new_row.append(round(element / div, 2))
            new_matrix.append(new_row)
        return new_matrix
