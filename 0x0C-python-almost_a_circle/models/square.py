#!/usr/bin/python3
'''Square Class definition'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square that inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class init'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Square information represintation'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size's Getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''Size's Setter'''
        self.width = value
        self.hight = value

def __update(self, id=None, size=None, x=None, y=None):
        '''update functin to check the inputed arguments'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update defifinition'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Class's dictionary representation'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
