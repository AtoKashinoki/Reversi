"""
    Reversi.Functions

This file contain functions for using in reversi processes.
"""

""" imports """


""" Convert functions """


class Convert:
    """ Convert functions """

    @staticmethod
    def index_from(_position2d: tuple[int, int], _length: int) -> int:
        """ Convert index from 2 dimension indexes """
        return _position2d[0] + _position2d[1] * _length

    @staticmethod
    def position2d_from(_index: int, _length: int) -> tuple[int, int]:
        """ Convert 2 dimension indexes from index """
        return _index%_length, _index//_length

    ...
