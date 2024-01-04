#!/usr/bin/python3
"""Define a class of rectanglar"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, data):
        """Width setter"""

        if type(data) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = data

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, data):
        """Height setter"""

        if type(data) != int:
            raise TypeError("height must be an integer")
        if data < 0:
            raise ValueError("height must be >= 0")
        self.__height = data
