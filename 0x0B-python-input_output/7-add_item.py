#!/usr/bin/python3
"""
this module  Load, add, save
"""
from sys import argv
load_from = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
i = 1
file = "add_item.json"

try:
    f = load_from(file)
except Exception:
    f = []

f.extend(argv[1:])
save(f, file)
