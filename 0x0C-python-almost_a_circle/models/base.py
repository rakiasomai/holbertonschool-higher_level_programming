#!/usr/bin/python3
"""class base
"""

import json


class Base:
    '''class base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json function'''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save function'''
        new_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for j in list_objs:
                new_list.append(j.to_dictionary())
        with open(filename, 'w') as fd:
            fd.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''from jason str function'''

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''it's the create function'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
