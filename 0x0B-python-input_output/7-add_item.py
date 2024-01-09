#!/usr/bin/python3
"""add_item Definition"""

import json
import os.path
from sys import argv
from os.path import exists
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    if exists(filename):
        json_list = load_from_json_file(filename)
    else:
        json_list = []
except FileNotFoundError:
    json_list = []

json_list.extend(argv[1:])

save_to_json_file(json_list, filename)
