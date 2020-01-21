#!/usr/bin/python3
def add_attribute(obj, i, y):
    rak = getattr(obj, "__doc__", None)
    if rak is None:
        setattr(obj, i, y)
    else:
        raise TypeError("can't add new attribute")
