#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None

    for row in matrix:
        if size is None:
            size=len(row)
        elif size!=len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(element/div,2) for element in row] for row in matrix]
