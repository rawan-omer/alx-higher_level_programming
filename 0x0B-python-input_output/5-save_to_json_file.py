#!/usr/bin/python3
"""save_to_json_file Definition"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
