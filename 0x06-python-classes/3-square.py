#!/usr/bin/python3
"""
This module provides a simple Square class with initialize size.
"""


class Square:
    """
    A class that defines a square by size and can compute area
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
