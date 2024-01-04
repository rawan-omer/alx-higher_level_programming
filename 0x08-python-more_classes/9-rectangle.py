#!/usr/bin/python3
"""Definetion of a Rectangle"""


class Rectangle:
    """Rectangle class defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = str(self.print_symbol) * self.__width
        alist = []
        for index in range(self.__height):
            alist.append(size)
        return "\n".join(alist)

    def __repr__(self):
        """Returns rectangle representation"""
        return "{:s}({:d}, {:d})".format((type(self).__name__),
                                         self.__width, self.__height)

    def __del__(self):
        """delete Rectangle, decrease the instances"""
        Rectangle.number_of_instances -= 1
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
        """Area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger regtangle"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return rectangle instance"""
        return cls(size, size)
