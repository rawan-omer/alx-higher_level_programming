#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """method must be implemented"""
        return self.__size ** 2

    def __str__(self):
        """representation of the string"""
        return f"[Square] {self.__size}/{self.__size}"
