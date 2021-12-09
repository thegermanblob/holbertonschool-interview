#!/usr/bin/python3
""" un metodo para abrir todas las cajas """

def canUnlockAll(boxes):
    """ checks if all boxes can be opened """
    keys = {0}
    for key in keys:
        for box in boxes[key]:
            if box not in keys:
                keys.add(box)
    return len(keys) == len(boxes)