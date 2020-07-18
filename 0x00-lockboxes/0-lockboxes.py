#!/usr/bin/python3
"""
This module contains the function canUnlockAll.
"""


def canUnlockAll(boxes):
    """
    Function that checks if all boxes can be unlocked.
    """
    boxes_amount = len(boxes)
    if boxes_amount == 1:
        return True
    locked = set([box for box in range(1, boxes_amount)])
    current_keys = [*boxes[0]]
    while current_keys:
        test_key = current_keys.pop()
        if test_key in locked:
            locked.remove(test_key)
            current_keys.extend(boxes[test_key])
        if not len(locked):
            return True
    return False
