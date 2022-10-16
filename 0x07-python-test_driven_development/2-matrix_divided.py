#!/usr/bin/python3
"""this module contains the matrix_divided function"""
def matrix_divided(matrix, div):
    """ return a new matrix

      Args:
          matrix (int): the list of lists
          div (int): the number that divides all element of the matrix

    """
    if type(matrix) is not list or  not len(matrix) > 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(item / div, 2) for item in row] for row in matrix]
    return result

