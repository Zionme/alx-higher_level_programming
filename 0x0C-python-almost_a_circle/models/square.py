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

    @property
    def size(self):
        """Return the size of the Square."""
        return self._width  # Use width as size

    @size.setter
    def size(self, value):
        """
        Set the size of the Square with the same value for width and height.
        """
        self._validate_positive_value(value, "size")  # Validate the value
        self._width = value  # Assign value to width
        self._height = value  # Assign value to height

    def __str__(self):
        """
        Return a string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # Additional helper method for value validation
    def _validate_positive_value(self, value, attr):
        """
        Validate that the given value is a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{attr} must be a positive integer")
