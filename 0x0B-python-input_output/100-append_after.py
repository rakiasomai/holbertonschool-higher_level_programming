#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    text = ""
    with open(filename, encoding="utf8") as fd:
        for lines in fd:
            text = text + lines
            if search_string in lines:
                text = text + new_string

    with open(filename, mode="w") as fd:
        fd.write(text)
