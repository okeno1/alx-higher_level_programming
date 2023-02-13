#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
Size defaults to 0. Raise errors on invalid inputs.
"""


class Square:

    """A class that defines a squuare by size"""

    def __init__(self, size=0):

        """
        The __init__ method for Square class

        Args:
           size: (:obj: 'int', optional): A private instance size

        Raises:
           TypeError: Exception if size is not an integer
           ValueError: Exception if size is less that 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
