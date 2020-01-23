#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    numb = 0
    with open(filename, encoding='utf-8') as fd:
        for lines in fd:
            numb = numb + 1
            print(lines, end="")
            if nb_lines == numb:
                break
