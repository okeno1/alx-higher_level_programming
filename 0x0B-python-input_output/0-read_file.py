#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module - 0-read_file
Reads a text file and print it out
"""


def read_file(filename=""):
    """
    Reads the file
    Arguments:
        filename (str): The name of the file to open
    """

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
