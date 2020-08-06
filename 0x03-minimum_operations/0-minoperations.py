#!/usr/bin/python3
"""
This module contains the function minOperations.
"""


def minOperations(n):
    """
    Calculates the minimum of operations of copy and paste to get
    n letters, starting with one.
    """
    count = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            count += divisor
            n //= divisor
        else:
            divisor += 1
    return count
