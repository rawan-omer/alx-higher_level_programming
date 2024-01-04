#!/usr/bin/python3
"""Rectangle class definetion"""


class Rectangle:
    """Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """The Rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        alist = []
        for index in range(self.__height):
            alist.append(size)
        return "\n".join(alist)

    def __repr__(self):
        """Returns representation of Rectangle"""
        return "{}({}, {})".format((type(self).__name__), self.__width,
                                   self.__height)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
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
        """returns the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height + self.__height) + (self.__width + self.__width)
