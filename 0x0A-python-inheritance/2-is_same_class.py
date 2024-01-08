#!/usr/bin/python3
"""is_same_class Function"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of class"""
    if type(obj) is a_class:
        return True
    else:
        return False
