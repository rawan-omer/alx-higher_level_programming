#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
