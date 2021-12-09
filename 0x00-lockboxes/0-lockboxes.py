#!/usr/bin/python3
""" un metodo para abrir todas las cajas """

def canUnlockAll(boxes):
    """ checks if all boxes can be opened """
    keys = [0]
    for key in keys:
        for n in boxes[key]:
            if n not in keys and n < len(boxes):
                keys.append(n)
    
    return len(keys) == len(boxes)
