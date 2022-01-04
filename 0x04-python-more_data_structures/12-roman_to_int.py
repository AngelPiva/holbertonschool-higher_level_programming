#!/usr/bin/python3
def roman_to_int(roman_string):
    romans_n = [
            ["I", 1],
            ["V", 5],
            ["X", 10],
            ["L", 50],
            ["C", 100],
            ["D", 500],
            ["M", 1000]
            ]
    total = 0
    for i in roman_string:
        for x in romans_n:
            if i == x[0]:
                total += x[1]
    return total
