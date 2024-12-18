"""
    Reversi.Objects

This file contain object classes for using in reversi processes.
"""


""" imports """


from abc import ABC, abstractmethod
from copy import copy
from typing import Any, Iterator
from .Definitions import IDX
from .Functions import Convert


""" Object skeletons """


class ObjectSkeleton(ABC):
    """ Reversi object skeleton """
    ...


class Entity(ObjectSkeleton):
    """ Reversi entity skeleton """

    """ values """
    __TEXTURE__: Any = None

    """ methods """
    # class
    @classmethod
    def __set_texture__(cls, _texture) -> None:
        cls.__TEXTURE__ = _texture
        return

    # instance
    @abstractmethod
    def __repr__(self) -> str:
        return ...

    ...


class Consept(ObjectSkeleton):
    """ Reversi consept skeleton """
    ...


""" Objects """


DISC_ID: dict[bool, int] = {True: 1, False: -1}


class Disc(Entity):
    """ Reversi disc """

    """ values """
    # class
    __TEXTURE__: tuple[str, str]
    __id: tuple[int, int] = (DISC_ID[False], DISC_ID[True])

    # instance
    __surface = True

    """ properties """
    @property
    def id(self) -> int: return self.__id[self.__surface]
    @property
    def surface(self) -> bool: return self.__surface

    """ methods """

    # instance
    def __init__(self, _surface: bool) -> None:
        """ Initialize disc values """
        self.__surface = _surface
        return

    def __repr__(self) -> str:
        return self.__TEXTURE__[self.__surface]

    def reverse(self) -> "Disc":
        self.__surface = not self.__surface
        return self

    def __eq__(self, other: "Disc") -> bool:
        return self.__surface == other.surface

    def __ne__(self, other: "Disc") -> bool:
        return self.__surface != other.surface

    def __neg__(self) -> "Disc":
        return copy(self).reverse()

    ...


EMPTY_ID = 0


class Empty(Entity):
    """ Reversi empty """

    """ values """
    # class
    __TEXTURE__: tuple[str, str]
    __id: int = EMPTY_ID
    __turn: int = -1

    # instance
    __possible_poss: list[tuple[int, int]]


    """ properties """
    @property
    def id(self) -> int: return self.__id
    @property
    def possible_poss(self) -> tuple[tuple[int, int], ...]:
        return tuple(self.__possible_poss)
    @possible_poss.setter
    def possible_poss(self, values: tuple[tuple[int, int]]) -> None:
        self.__possible_poss += list(values)
        return

    """ methods """

    # instance
    def __init__(self):
        """ Initialize disc values """
        self.__possible_poss = []
        return

    def __repr__(self) -> str:
        return self.__TEXTURE__[len(self.__possible_poss)>0]

    def set_possible_poss(self, value: tuple[tuple[int, int], ...]):
        self.__possible_poss = list(value)
        return

    ...


class Board(Entity):
    """ Reversi board """

    """ values """
    # class
    __TEXTURE__: str

    # instance
    __size: tuple[int, int]
    __data: list

    """ properties """
    @property
    def size(self) -> tuple[int, int]: return self.__size
    @property
    def data(self) -> list: return self.__data

    """ methods """

    # instance
    def __init__(self, size: tuple[int, int] = (8, 8)):
        """ Initialize values """
        self.__size = size
        self.__data = [Empty() for _ in range(size[IDX.X]*size[IDX.Y])]
        return

    def __repr__(self) -> str:
        return self.__TEXTURE__.format(*self.__data)

    def get_data(self) -> list[list[bool | None]]:
        return \
            [
                [
                    d.id
                    for d in self.__data[
                             idx*self.size[IDX.X]:(idx+1)*self.size[IDX.X]
                    ]
                ]
                for idx in range(self.size[IDX.Y])
            ]

    # container
    def __getitem__(
            self, _pos: tuple[int, int],
    ) ->  Disc | Empty:
        return self.__data[
            Convert.index_from(_pos, self.__size[IDX.X])
        ]

    def __setitem__(
            self, _pos: tuple[int, int], _value: Disc | Empty,
    ) -> None:
        self.__data[
            Convert.index_from(_pos, self.__size[IDX.X])
        ] = _value

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> Iterator[Disc]:
        return iter(self.__data)

    def __contains__(self, _item: Disc) -> bool:
        return _item in self.__data

    ...
