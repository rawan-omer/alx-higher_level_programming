#!/usr/bin/python3
'''Rectangle class defintion'''
from models.base import Base


class Rectangle(Base):
    '''the Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''the main definition'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for the width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for the hight'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns the rectangle's area'''
        return self.width * self.height

    def display(self):
        '''prints the Rectangle instance with the character #'''
        dis = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(dis, end='')

    def __str__(self):
        '''Returns formating for rectangle's informations.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Updates instance attributes definition'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''ssigns an argument to each attribute'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Convert to dictionary'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
