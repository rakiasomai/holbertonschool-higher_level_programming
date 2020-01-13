#!/usr/bin/python3
'''
This is a function called "add_integer"  
This function contains 2 elements (a, b) 
the retun must be an integer.
'''


def add_integer(a, b):
    '''Return the sum of two integers or floats as an integer.
    '''
    m = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(m):
        return int(a) + int(b)

    for y, z in list(zip(m, ['a', 'b'])):
        if not y:
            raise TypeError("{} must be an integer".format(z))
