#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.
        """
        super().__init__(id) # Call the super class with id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter and Setter for width attribute
    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be a positive integer.")

    # Getter and Setter for height attribute
    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be a positive integer.")

    # Getter and Setter for x attribute
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    # Getter and Setter for y attribute
    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    # Property decorators for accessing attributes using getters and setters
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    x = property(get_x, set_x)
    y = property(get_y, set_y)

