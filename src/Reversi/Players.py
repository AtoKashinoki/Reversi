"""
    Reversi.Players

This file contain player classes for using reversi.
"""


""" imports """


from abc import ABC, abstractmethod
from random import randrange
from .Definitions import IDX
from .Game import Reversi1v1


""" Player skeleton """


class PlayerSkeleton(ABC):
    """ Player class skeleton """

    """ values """
    __game = None

    """ properties """
    @property
    def game(self): return self.__game

    """ methods """

    def _set_game(self, value):
        self.__game = value
        return

    @abstractmethod
    def __input__(self) -> tuple[int, int]: ...

    ...


""" Human """


class Human(PlayerSkeleton):
    __game: Reversi1v1

    def __init__(self):
        return

    def __input__(self):
        _input =()
        done = False
        while not done:
            done = True
            possible_poss = tuple(map(
                lambda pos: (pos[IDX.X]+1, pos[IDX.Y]+1),
                self.game.possible_poss
            ))
            print(f"{possible_poss=}")
            print("input: ", end="")
            _input = tuple(input().split(" "))
            _input = tuple(d for d in _input if not d == "")
            try: _input = tuple(map(int, _input))
            except ValueError: done = False
            if not len(_input) == 2: done = False
            if not done: print("Try again.")
            continue

        return tuple(map(lambda _val: _val-1 , _input))

    ...


""" AI """


class RandomAI(PlayerSkeleton):

    """ values """
    game: Reversi1v1

    def __init__(self):
        return

    def __input__(self):
        possible_poss = self.game.possible_poss
        input_ = possible_poss[randrange(len(possible_poss))]
        print(
            f"{self.__class__.__name__} input.\n"
            f"{possible_poss=}\n"
            f"{input_=}\n"
        )
        return input_

    ...
