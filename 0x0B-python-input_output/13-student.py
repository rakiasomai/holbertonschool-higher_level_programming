#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {rslt: value for rslt, value in self.__dict__.items()
                    if rslt in attrs}

    def reload_from_json(self, json):
        return self.__dict__.update(json)
