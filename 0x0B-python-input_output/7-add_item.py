#!/usr/bin/python3
"""add_item Definition"""

import json
import os.path
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

alist = []

if os.path.exists(filename):
    alist = load_from_json_file(filename)

for i in argv[1:]:
    alist.append(i)

save_to_json_file(alist, filename)
