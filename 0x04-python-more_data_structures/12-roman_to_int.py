#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
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
    actual = 0
    for i in roman_string:
        for x in romans_n:
            if i == x[0]:
                if actual == 0 or actual >= x[1]:
                    total += x[1]
                else:
                    total += x[1] - (actual * 2)
                actual = x[1]
    return total
