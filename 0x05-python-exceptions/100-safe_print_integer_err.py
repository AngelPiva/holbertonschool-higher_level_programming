#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError) as verror:
        print("Exception: " + str(verror), file = sys.stderr)
        return False
