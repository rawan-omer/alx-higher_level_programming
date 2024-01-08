#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle Class"""


class Rectangle(BaseGeometry):
    """Rectangle class  that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height:"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method must be implemented"""
        return (self.__width * self.__height)

    def __str__(self):
        """The represimtation of the String"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
