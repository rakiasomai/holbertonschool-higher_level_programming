#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        z = 0
        for y in range(x):
            if isinstance(my_list[y], int):
                z += 1
                print("{:d}".format(my_list[y]), end="")
    except TypeError as err:
        print(err)
    else:
        print("")
        return z
