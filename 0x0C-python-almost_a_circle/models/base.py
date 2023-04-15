#!/usr/bin/python3
"""Defines a base model class."""
import os


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
