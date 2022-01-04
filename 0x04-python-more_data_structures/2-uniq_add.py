#!/usr/bin/python3
def uniq_add(my_list=[]):
    once = set(my_list)
    add = 0
    for i in once:
        add += i
    return add
