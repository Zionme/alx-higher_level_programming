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
        super().__init__(id)  # Call the super class with id
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and Setter for width attribute
    def get_width(self):
        return self.__width

    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer.")
        if width <= 0:
            raise ValueError("Width must be > 0.")
        self.__width = width

    # Getter and Setter for height attribute
    def get_height(self):
        return self.__height

    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("Height must be an integer.")
        if height <= 0:
            raise ValueError("Height must be > 0.")
        self.__height = height

    # Getter and Setter for x attribute
    def get_x(self):
        return self.__x

    def set_x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer.")
        if x < 0:
            raise ValueError("x must be >= 0.")
        self.__x = x

    # Getter and Setter for y attribute
    def get_y(self):
        return self.__y

    def set_y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer.")
        if y < 0:
            raise ValueError("y must be >= 0.")
        self.__y = y

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    # Property decorators for accessing attributes using getters and setters
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    x = property(get_x, set_x)
    y = property(get_y, set_y)
