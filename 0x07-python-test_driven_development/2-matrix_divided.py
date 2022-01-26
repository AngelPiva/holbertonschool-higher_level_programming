#!/usr/bin/python3
"""
matrix_divide module
"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    new_matrix = []
    exception1 = "matrix must be a matrix (list of lists) of integers/floats"
    div_req(div)
    if type(matrix) is not list:
        raise TypeError(exception1)

    for elem in matrix:
        new_elem = []
        if type(elem) is not list:
            raise TypeError(exception1)
        if len(elem) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for sub_elem in elem:
            if type(sub_elem) is not int and type(sub_elem) is not float:
                raise TypeError(exception1)
            new_elem.append(round(sub_elem / div, 2))
        new_matrix.append(new_elem)
    return new_matrix


def div_req(div):
    """ divide requirements """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
