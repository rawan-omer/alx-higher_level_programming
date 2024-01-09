#!/usr/bin/python3
"""class_to_json Definition"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return vars(obj)
