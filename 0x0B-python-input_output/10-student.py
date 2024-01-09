#!/usr/bin/python3
"""Student class Difinition"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init for student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation """
        if attrs is None:
            return self.__dict__

        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary
