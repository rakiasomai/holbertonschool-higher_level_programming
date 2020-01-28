#!/usr/bin/python3
'''square file'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''def init'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''def  size'''
        return self.width

    @size.setter
    def size(self, value):
        '''def size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''def str'''
        return "[square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        '''def update'''
        if len(args):
            for z, arg in enumerate(args):
                if z == 0:
                    self.id = arg
                elif z == 1:
                    self.size = arg
                elif z == 2:
                    self.x = arg
                elif z == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''def to dictionary'''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
