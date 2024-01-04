#!/usr/bin/python3
"""Rectangle class definetion"""


class Rectangle:
    """Rectangle that defines a rectangle"""
    rect_num = 0

    def __init__(self, width=0, height=0):
        """The Rectangle"""
        self.width = width
        self.height = height
        Rectangle.rect_num += 1

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
        return "{:s}({:d}, {:d})".format((type(self).__name__),
                                         self.__width, self.__height)

    def __del__(self):
        """delete the Rectangle by decrease it"""
        Rectangle.rect_num -= 1
        print("Bye rectangle...")

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
        return 2 * (self.__width + self.__height)
