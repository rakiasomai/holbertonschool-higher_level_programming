#!/usr/bin/python3
"""
module of class student
"""


class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dictionary representation
        """
        return (self.__dict__)
