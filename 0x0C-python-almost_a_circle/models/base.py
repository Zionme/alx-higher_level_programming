#!/usr/bin/python3
"""Defines a base model class."""
import os
import json


# Create a folder named models with an empty file __init__.py inside
if not os.path.exists('models'):
    os.makedirs('models')
    open('models/__init__.py', 'w').close()


class Base:
    # Private class attribute __nb_objects
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        if id is not None:
            # Assign id to the public instance attribute id
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static method to convert list of dictionaries to JSON string
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            # Return "[]" for None or empty list_dictionaries
            return "[]"
        else:
            # Return JSON string representation of list_dictionaries
            return json.dumps(list_dictionaries)

    # Class method to save list_objs to a file
    @classmethod
    def save_to_file(cls, list_objs):
        # Get the class name
        class_name = cls.__name__
        # Create a list to store dictionaries of list_objs
        list_dicts = []
        if list_objs is not None:
            # Convert list_objs to list of dictionaries
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        # Convert list_dicts to JSON string
        json_string = cls.to_json_string(list_dicts)

        # Write the JSON string to a file
        filename = "{}.json".format(class_name)
        with open(filename, 'w') as file:
            file.write(json_string)
