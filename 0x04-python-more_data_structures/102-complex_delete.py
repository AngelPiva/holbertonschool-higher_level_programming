#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return a_dictionary
    new_dict = []

    for n, i in a_dictionary.items():
        if i == value:
            new_dict.append(n)
    for x in new_dict:
        del a_dictionary[x]
    return a_dictionary
