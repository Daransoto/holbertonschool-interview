#!/usr/bin/python3
""" This module contains the function validUTF8. """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    i = 0
    ld = len(data)
    while i < ld:
        if data[i] & 0x80 == 0:
            i += 1
        elif data[i] & 0xc0 == 0x80:
            return False
        else:
            test = 0x40
            count = 0
            while data[i] & test:
                count += 1
                test >>= 1
            i += 1
            for _ in range(count):
                if i >= ld or data[i] & 0x80 != 0x80:
                    return False
                i += 1
    return i == ld
