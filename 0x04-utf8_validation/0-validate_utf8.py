#!/usr/bin/python3
""" 0. UTF-8 Validation """


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encodin:1
    """
    try:
        bytes(data)
    except ValueError:
        return False

    return True
