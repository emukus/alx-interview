#!/usr/bin/python3
"""
This module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """A method that determines if all the boxes can be opened
        Param:
            boxes: a list of lists.
    """
    box = len(boxes) * [False]
    box[0] = True
    keys = 0

    for each in keys:
        for i in boxes[each]:
            if i not in keys:
                if i < len(boxes):
                    box[i] = True
                    keys.append(i)
    return all(box)
