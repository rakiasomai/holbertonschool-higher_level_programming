#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = my_dictionary.copy()
    for y, z in copy.items():
        if value in z:
            del a_dictionary[y]
    return a_dictionary
