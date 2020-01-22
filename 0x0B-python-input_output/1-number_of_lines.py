#!/usr/bin/python3
def number_of_lines(filename=""):
    numb = 0
    with open(filename, encoding="utf-8") as fd:
        for lines in fd:
            numb += 1
    return numb
