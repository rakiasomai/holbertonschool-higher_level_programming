#!/usr/bin/python3
'''
This is a function called "say my name"
This function takes one required parameter & one optional.
The output is "My name is (first) (last)" where (first) & (last) are the arguments.
'''


def say_my_name(first_name, last_name=""):
    '''
    Print My name is (first name) (last name) if given, else print error.
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
