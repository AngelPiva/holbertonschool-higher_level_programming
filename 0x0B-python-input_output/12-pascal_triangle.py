#!/usr/bin/python3
"""
module
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing 
    the Pascal’s triangle of n
    """
    pascal = [[1]]
    if n <= 0:
        return []
    for i in range(n):
        if i != n - 1:
            pascal.append([1])
        if i >= 1:
            for x in range(1, i):
                pascal[i].append(pascal[i - 1][x - 1] + pascal[i - 1][x])
            pascal[i].append(1)
    return pascal
