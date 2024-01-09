#!/usr/bin/python3
"""from_json_string Definition"""


import json


def from_json_string(my_str):
    """opject represented by a JSON string"""
    return json.loads(my_str)
