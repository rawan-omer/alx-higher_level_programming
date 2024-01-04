#!/usr/bin/python3
"""definition of class Rectangle"""


class Rectangle:
    """Rectangle class that defines a rectangle"""
    i = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.i += 1

    def __str__(self):
        """prints the rectangle with the character(s) stored"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = str(self.print_symbol) * self.__width
        alist = []
        for index in range(self.__height):
            alist.append(size)
        return "\n".join(alist)

    def __repr__(self):
        """the rectangle representation"""
        return "{:s}({:d}, {:d})".format((type(self).__name__),
                                         self.__width, self.__height)

    def __del__(self):
        """delete the Rectangle"""
        Rectangle.i -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """the width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """the height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the larger rectangle after comparing"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
