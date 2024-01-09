#!/usr/bin/python3
"""load_from_json_file Definition"""


import json


def load_from_json_file(filename):
    """Creates an Object from json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
