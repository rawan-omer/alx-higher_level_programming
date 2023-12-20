#!/usr/bin/python3


class Square:
    """Class Square that defines a square.

    Attributes:
        __size: The square's size
    """

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size: The square's size
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value: The square's size

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if self.__validate_size(value):
            self.__size = value

    def __validate_size(self, size):
        """Validate the size attribute.

        Args:
            size: The square's size

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        return True

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
