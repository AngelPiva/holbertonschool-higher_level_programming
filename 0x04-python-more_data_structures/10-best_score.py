#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = []
    max_value = 0
    for i in a_dictionary:
        if a_dictionary[i] > max_value:
            max_key = i
            max_value = a_dictionary[i]
    return max_key
