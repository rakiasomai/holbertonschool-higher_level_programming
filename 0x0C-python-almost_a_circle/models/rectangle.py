#!/usr/bin/python3
'''file Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''init rectangle'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''proprety width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''proprety heighet'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''proprty x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''prprety y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''def area'''
        return self.__width * self.__height

    def display(self):
        '''de display'''
        print("\n" * self.y, end="")
        for z in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''def str'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        '''def update'''
        if len(args):
            for z, arg in enumerate(args):
                if z == 0:
                    self.id = arg
                elif z == 1:
                    self.width = arg
                elif z == 2:
                    self.height = arg
                elif z == 3:
                    self.x = arg
                elif z == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        '''def to dictionary'''
        return {
            "id": self.id,
            "height": self.height,
            "x": self.x,
            "y": self.y,
            "width": self.width
        }
