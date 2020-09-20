#!/usr/bin/python3
""" This module contains the function validUTF8. """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    i = 0
    ld = len(data)
    count = 0
    while i < ld:
        byte = data[i] & 0xff
        if byte & 0x80 == 0:
            i += 1
        elif byte & 0xc0 == 0x80:
            return False
        else:
            test = 0x40
            while byte & test:
                count += 1
                test >>= 1
            i += 1
            for _ in range(count):
                byte = data[i] & 0xff
                if i >= ld or byte & 0x80 != 0x80:
                    return False
                i += 1
    return count == 0
