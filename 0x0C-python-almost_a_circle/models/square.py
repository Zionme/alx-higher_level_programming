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

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square object with *args and/or **kwargs.
        """
        if args:
            if len(args) > 4:
                raise ValueError("update() takes at most 4 positional arguments
                                 (id, size, x, y)")
            self.id = args[0] if args[0] is not None else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
        else:
            if 'id' in kwargs:
                self.id = kwargs['id'] if kwargs['id'] is not None else self.id
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

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
