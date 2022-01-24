#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    average = 0
    division = 0
    for i in my_list:
        average += (i[0] * i[1])
        division += i[1]
    return average / division
