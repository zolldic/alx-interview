#!/usr/bin/python3
""" 0. UTF-8 Validation """


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encodin:1
    """
    bytes_number = 0
    for byte in data:
        if byte < 0 or byte > 255:
            return False

        lsb = byte & 0b11111111

        if bytes_number == 0:
            if lsb < 0x80:
                bytes_number = 0
            elif lsb < 0xC2:
                return False
            elif lsb < 0xE0:
                bytes_number = 2
            elif lsb < 0xF0:
                bytes_number = 3
            else:
                return False
        else:
            if lsb < 0x80:
                return False
            bytes_number -= 1
    return bytes_number == 0
