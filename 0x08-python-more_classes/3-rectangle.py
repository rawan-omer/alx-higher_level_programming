#!/usr/bin/python3
"""Just Rectangle class"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Rectangle """
        self.width = width
        self.height = height

    def __str__(self):
        """prints rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        alist = []
        for index in range(self.__height):
            alist.append(size)
        return "\n".join(alist)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height * self.__height) + (self.__width * self.__width)
