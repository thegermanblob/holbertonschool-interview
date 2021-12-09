#!/usr/bin/env python3

def canUnlockAll(boxes):
    """ checks if all boxes can be opened """
    keys = [0]
    for box in boxes:
        if box not in keys:
            keys = keys + box
    return len(keys) == len(boxes)