#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for y, v in my_dict.items():
        new_dict[y] = v * 2
    return new_dict
