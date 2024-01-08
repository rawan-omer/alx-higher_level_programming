#!/usr/bin/python3
"""lookup method"""


def lookup(obj):
    """ function that returns the list of available attributes"""
    return [i for i in dir(obj)]
