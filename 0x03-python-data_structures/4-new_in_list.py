#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list.copy()
    if idx < 0:
        return cpy
    if idx > len(my_list) - 1:
        return cpy
    for i in my_list:
        if i == idx:
            cpy[i] = element
            return cpy
