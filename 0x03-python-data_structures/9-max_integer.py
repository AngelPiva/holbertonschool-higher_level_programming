#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    x = min(my_list)
    for i in my_list:
        if i > x:
            x = i
    return x
