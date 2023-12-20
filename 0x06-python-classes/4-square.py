#!/usr/bin/python3

class Square:
	"""Class Square that defines a square"""
	def __init__(self, size=0):
		"""Initialises the data

		Args:
		size: The square's size
		"""
		self.size = size

	def area(self):
		"""Returns the area of square"""
		return self.__size**2

	@property
	def size(self):
		"""Getter method for the size attribute."""
		return self.__size

	@size.setter
	def size(self, value):
		"""Setter method

		Args:
			value: The square's size
		Raises:
			TypeError: If size is not an integer.
			ValueError: If size is less than 0.
		"""
		self.__size = value
	if type(value) != int:
		raise TypeError("size must be an integer")
	if value < 0:
		raise ValueError("size must be >= 0")
