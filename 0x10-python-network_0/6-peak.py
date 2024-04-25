#!/usr/bin/python3
"""
Module to find the highest number in an array
"""


def find_peak(list_of_integers):
    """
    Method to find the highest number in array
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
