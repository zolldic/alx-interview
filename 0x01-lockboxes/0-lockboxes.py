#!/usr/bin/python3
"""  0. Lockboxes """


def canUnlockAll(boxes):
    """ function that determines if all the boxes can be opened. """
    sets = {0}
    for idx, box in enumerate(boxes):
        for key in box:
            if key != idx:
                sets.add(key)

    if len(sets) == len(boxes):
        return True
    else:
        return False
