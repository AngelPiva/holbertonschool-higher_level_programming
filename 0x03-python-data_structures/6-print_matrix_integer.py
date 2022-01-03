#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements in matrix:
            x = 1
            for element in elements:
                if x == len(elements):
                    print('{:d}'.format(element), end='')
                else:
                    print('{:d}'.format(element), end=' ')
                x += 1
            print()
