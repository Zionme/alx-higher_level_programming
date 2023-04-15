#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object with given size, x, y, and id.
        """
        super().__init__(size, size, x, y, id)
        # Call the super class with id, x, y, width and height
        self.width = size  # Assign size to width
        self.height = size  # Assign size to height

    def __str__(self):
        """
        Return a string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
