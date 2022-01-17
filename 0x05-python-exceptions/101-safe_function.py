#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = 0
    try:
        result = fct(*args)
    except ZeroDivisionError:
        result = None
        print("Exception: division by zero", file=sys.stderr)
    except IndexError:
        result = None
        print("Exception: list index out of range", file=sys.stderr)
    finally:
        return result
