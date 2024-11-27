#!/usr/bin/python3
"""
Method to determine if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]  # Start with the first box unlocked

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
