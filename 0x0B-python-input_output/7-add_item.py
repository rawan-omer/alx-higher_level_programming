#!/usr/bin/python3
"""add_item Definition"""


import sys
from os.path import exists
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

alist = list(sys.argv[1:])
try:
    if exists('add_item.json'):
        old_data = load_from_json_file('add_item.json')
    else:
        old_data = []
except FileNotFoundError:
    old_data = []

old_data.extend(alist)
save_to_json_file(old_data, 'add_item.json')
