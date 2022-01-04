#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    for i in cpy:
        cpy[i] = a_dictionary[i] * 2
    return cpy
