#!/usr/bin/python3
"""Student class Defintion"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init for student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """etrieves a dictionary representation"""
        return self.__dict__
