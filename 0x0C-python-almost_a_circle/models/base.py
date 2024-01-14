#!/usr/bin/python3
"""Base class definition"""


class Base:
    """class will be the base of all other classes in this project."""
    __nb_objects = 0
    def __init__(self, id=None):
        """function to manage id attribute"""
        if id is not None:
            id.self = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
