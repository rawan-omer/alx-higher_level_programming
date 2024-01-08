#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry (based on 6-base_geometry.py)."""
    def area(self):
        """raises an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
