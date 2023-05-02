#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json


from save_to_json_file = __import__('5-load_to_json_file').save_to_json_file
from load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    # load existing list from file, if it exists
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # create a new list if file does not exist
    my_list = []

# add all arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# save the list to file in JSON format
save_to_json_file(my_list, filename)
