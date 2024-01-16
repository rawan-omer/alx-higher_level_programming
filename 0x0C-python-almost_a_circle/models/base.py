#!/usr/bin/python3
"""Base class definition"""
import json
import csv
from os import path


class Base:
    """class will be the base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """function to manage id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fl:
            fl.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            alist = Rectangle(1, 1)
        elif cls is Square:
            alist = Square(1)
        else:
            alist = None
        alist.update(**dictionary)
        return alist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes and deserializes in CSV'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''returns a list of instances'''
        from models.rectangle import Rectangle
        from models.square import Square
        dum = []
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as file:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
