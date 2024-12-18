"""
    Types

This file contain types.
"""


""" imports """


from typing import Any


""" Log list """


class Log(list):
    """ Log list """

    """ values """
    __length: int

    """ properties """
    @property
    def length(self): return self.__length

    """ methods """

    def __init__(self, _length: int) -> None:
        """ Initialize list and values """
        super().__init__()
        self.__length = _length
        return

    def append(self, _value: Any) -> Any:
        """
            Append value to list and
            delete any data that exceeds the length
        """
        super().append(_value)
        if not len(self) > self.__length: return
        return self.pop(0)

    def undo(self) -> bool:
        """
            remove the last value of list and
            return whether the deletion was successful
        """
        if not len(self) > 0: return False
        del self[-1]
        return True

    ...
