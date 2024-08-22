#!/usr/bin/python3
""" 0. UTF-8 Validation """


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encodin:1
    """
    bytes_number = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        lsb = byte & 0b11111111

        if bytes_number == 0:
            if (lsb & mask1) == 0:
                continue
            elif (lsb & mask1) != 0 and (lsb & mask2) == 0:
                return False
            else:
                bytes_number = 0
                mask = mask1
                while (byte & mask) != 0:
                    bytes_number += 1
                    mask >>= 1

                if bytes_number == 1 or bytes_number > 4:
                    return False
        else:
            if not (byte & mask1 != 0 and byte & mask2 == 0):
                return False
        bytes_number -= 1
    return bytes_number == 0
