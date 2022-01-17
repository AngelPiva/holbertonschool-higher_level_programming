#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    size = 0
    i = 0
    try:
        for i in my_list:
            if (size < x):
                print(i, end="")
                size += 1
        print()
    except:
        pass
    finally:
        return (size)
