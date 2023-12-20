#!/usr/bin/python3

class Square:
    """Class Square that defines a square.

    Attributes:
        __size: The length of the square
    """

    def __init__(self, size=0):
        """Initializes

        Args:
            size: The length of the square's sides
        """
        self.size = size

    @property
    def size(self):
        """Getter to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size attribute.

        Args:
            value: The length of the square's

        Raises:
            TypeError: If size not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the square area."""
        return self.__size ** 2
