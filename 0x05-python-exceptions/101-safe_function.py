#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        y = fct(*args)
    except Exception as er:
        y = None
        print("Exception: {}".format(er), file=sys.stderr)
    finally:
        return y
