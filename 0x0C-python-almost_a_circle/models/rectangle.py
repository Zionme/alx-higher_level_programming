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

    # Property decorators for accessing attributes using getters and setters
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle with '#' characters in stdout.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Returns the string representation of the Rectangle instance.
        Returns:
            str: The string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

        def update(self, *args, **kwargs):
        """
        Updates the Rectangle using no-keyword and key-worded arguments.
        Args:
            *args: Arguments in the order: id, width, height, x, y.
            **kwargs: Key-worded argument to be updated.
        """
        if args:
            # If *args exists and is not empty, update attributes using
            # no-keyword arguments
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        if kwargs:
            # Update attributes using key-worded arguments
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle instance.
        Returns:
            dict: The dictionary representation of the Rectangle instance.
        """
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
        }
