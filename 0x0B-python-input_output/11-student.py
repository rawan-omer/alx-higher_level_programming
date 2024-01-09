#!/usr/bin/python3
"""Student class Definition"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Initialize Student class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance"""
        if attrs is None:
            return self.__dict__

        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        """Reload attributes from a JSON representation"""
        for key, value in json.items():
            setattr(self, key, value)
