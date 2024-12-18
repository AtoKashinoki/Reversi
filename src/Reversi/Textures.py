"""
    Reversi.Textures

This file contain texture programs for using reversi processes.
"""


""" imports """


from abc import ABC, abstractmethod
from typing import Any
from .Objects import Disc, Empty, Board
from .Definitions import IDX
from .ANSI import Tex, F, FC, BC, texture


""" Skeleton """


class TextureSkeleton(ABC):
    """ Reversi texture pack skeleton """

    """ textures """
    __textures: dict[type[Disc | Empty | Board], Any] = {
        Disc: None, Empty: None, Board: None
    }

    @property
    def textures(self) -> dict[type[Disc | Empty | Board], Any]:
        return self.__textures

    @abstractmethod
    def __init__(self): ...

    def __call__(self):
        [
            key.__set_texture__(value)
            for key, value in self.__textures.items()
        ]
        return

    ...


""" console texture """


class ConsoleTexture(TextureSkeleton):
    """ Print console """

    def __init__(self, _size: tuple[int, int]):
        self.disc_texture()
        self.empty_texture()
        self.board_texture(_size)
        return

    def disc_texture(self):
        self.textures[Disc] = (
            f"{FC.WHITE}〇", f"{FC.BLACK}〇"
        )
        return

    def empty_texture(self):
        self.textures[Empty] = (
            "　", f"{FC.MAGENTA}✖",
        )
        return

    def board_texture(self, _size: tuple[int, int]):
        board_c = (f"{BC.GREEN}", f"{texture(102)}")

        board_tex = ""
        for y in range(_size[IDX.Y]):
            board_tex += f"\n"
            for x in range(_size[IDX.X]):
                board_tex += board_c[(y+x)%2]+"{}"
                continue
            board_tex += f"{Tex.CLEAR}"
            continue

        self.textures[Board] = board_tex
        return

    ...
