"""
    Reversi.Definitions

This file contain definitions for using in reversi processes.
"""


""" imports """


""" Index and key """


class IDX:
    """ Index definitions """
    X, Y, Z = range(3)
    ...


""" direction """


DIRECTION = tuple(
    (x, y)
    for y in range(-1, 2)
    for x in range(-1, 2)
    if not (x, y) == (0, 0)
)

