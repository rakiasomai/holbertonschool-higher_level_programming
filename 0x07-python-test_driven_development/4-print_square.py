#!/usr/bin/python3
'''
This function called "Print Square" 
this function prints a square using this symbol "#"
The arguments must be an integer
'''


def print_square(size):
    ''' 
    Print a square by using arguments
    '''
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))
