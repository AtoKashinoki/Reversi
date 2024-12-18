"""
    Reversi.Game

This file contain reversi game programs.
"""


""" imports """


from copy import deepcopy
from .Objects import (
    Consept, Board, Disc, Empty, DISC_ID, EMPTY_ID
)
from .Textures import TextureSkeleton, ConsoleTexture
from .Types import Log
from .Definitions import IDX, DIRECTION
from .Functions import Convert


""" Reversi game """


class Reversi(Consept):
    """ Reversi game """

    """ values """
    # class
    __board_size: tuple[int, int] = None
    __initial_disc_pos: dict[tuple[ int, int], Disc] = {}

    # instance
    __board: Board
    __possible_poss: tuple[tuple[int, int], ...]
    __move_log: Log[tuple[tuple[int, int], bool], ...]

    """ properties """

    @property
    def possible_poss(self) -> tuple[tuple[int, int], ...]:
        return self.__possible_poss

    """ methods """
    # class
    @classmethod
    def set_board_size(cls, _size: tuple[int, int]) -> None:
        cls.__board_size = _size
        return

    @classmethod
    def set_initial_disc_pos(
            cls, _discs: dict[tuple[int, int], Disc]
    ) -> None:
        cls.__initial_disc_pos = _discs
        return

    # statick
    @staticmethod
    def set_texture(texture_pack: TextureSkeleton) -> None:
        texture_pack()
        return

    # instance
    def __init__(self, _log_depth: int):
        """ Initialize reversi game """
        # possible_pos
        self.__possible_poss = ()
        # log
        self.__move_log = Log(_log_depth)
        # board
        self.init_board()
        return

    def init_board(self):
        """ Initialize board """
        if self.__board_size is None:
            raise ValueError("Board size is None")
        self.__board = Board(self.__board_size)
        [
            self.__board.__setitem__(_pos, _value)
            for _pos, _value in self.__initial_disc_pos.items()
        ]
        self.update_possible_position(True, self.__board)
        return

    def get_board(self) -> Board:
        _value = None
        board = deepcopy(self.__board)
        for _pos, _value in self.__move_log:
            print(_pos, _value)
            self.update_possible_position(_value, board)
            self.__reverse_disc(_pos, _value, board)
            board.__setitem__(_pos, Disc(_value))
            continue
        self.update_possible_position(not _value, board)
        return board

    @staticmethod
    def __reverse_disc(
            _pos: tuple[int, int], _value: bool, board: Board
    ) -> None:
        [
            board[pos].reverse()
            for pos in board[_pos].possible_poss
        ]
        return

    @staticmethod
    def __get_exploration_pos(
            _board: Board, _length: int, _surface: bool
    ) -> tuple[tuple[int, int], ...]:
        return tuple(
            Convert.position2d_from(idx, _length)
            for idx, value in enumerate(_board)
            if isinstance(value, Disc)
            if value.id == DISC_ID[_surface]
        )

    def __explore_direction(
            self,
            _target: tuple[int, int],
            _board: Board,
            _surface: bool,
            _max_depth: int,
    ) -> tuple[tuple[int, int], ...]:
        x, y = _target
        enemy = not _surface
        poss = []

        for dx, dy in DIRECTION:

            reverse_disc = []
            for diff in range(1, _max_depth):
                _pos = x+dx*diff, y+dy*diff
                if (
                        not 0 <= _pos[IDX.X] < self.__board_size[IDX.X] or
                        not 0 <= _pos[IDX.Y] < self.__board_size[IDX.Y]
                ): continue
                _id = _board[_pos].id

                if _id == DISC_ID[enemy]:
                    reverse_disc.append(_pos)
                    continue
                if not diff > 1: break
                if not _id == EMPTY_ID:  break
                _board[_pos].possible_poss = reverse_disc
                poss.append(_pos)
                break

            continue

        return tuple(poss)

    def update_possible_position(
            self, _surface: bool, board: Board
    ) -> None:
        """ Update Empty of possible position"""

        # get target to explore
        length = self.__board_size[IDX.X]
        targets = self.__get_exploration_pos(board, length, _surface)

        # reset Empty
        [
            board[x, y].set_possible_poss(())
            for y in range(self.__board_size[IDX.Y])
            for x in range(self.__board_size[IDX.X])
            if isinstance(board[x, y], Empty)
        ]

        # explore and update empties
        self.__possible_poss = tuple(
            pos
            for target in targets
            for pos in self.__explore_direction(
                target, board, _surface, max(self.__board_size)
            )
        )
        return

    def put_disc(self, _pos: tuple[int, int], _surface: bool) -> bool:
        if not _pos in self.__possible_poss: return False
        exceeds = self.__move_log.append((_pos, _surface))
        if exceeds is not None:
            self.__reverse_disc(exceeds[0], exceeds[1], self.__board)
            self.__board.__setitem__(exceeds[0], exceeds[1])
            ...
        return True

    def undo(self) -> bool:
        """
            remove the last log and
            return whether the deletion was successful
        """
        return self.__move_log.undo()

    def __repr__(self):
        return self.get_board().__repr__()

    ...


""" Reversi game """


class Reversi1v1:
    """ Reversi game 1vs1 """

    """ values """
    # class
    initial_disc_pos: dict[tuple[ int, int], Disc] = dict(zip(
        [(3, 3), (3, 4), (4, 3), (4, 4)],
        [Disc(False), Disc(True), Disc(True), Disc(False)],
    ))
    texture: type[TextureSkeleton] = ConsoleTexture

    # instance
    __reversi: Reversi
    __players: tuple
    __turn: int
    __pass_count: int

    """ properties """
    @property
    def players(self) -> tuple: return self.__players
    @property
    def possible_poss(self) -> tuple[tuple[int, int], ...]:
        return self.__reversi.possible_poss

    """ methods """

    # instance
    def __init__(
            self, _players: tuple, size: tuple[int, int] = (8, 8)
    ):
        """ Initialize reversi game """

        # reversi
        ## boards and discs
        Reversi.set_board_size(size)
        Reversi.set_initial_disc_pos(self.initial_disc_pos)
        ## texture
        Reversi.set_texture(self.texture(size))
        ## init
        self.__reversi = Reversi(size[IDX.X]*size[IDX.Y]-4)

        # players
        self.__players = _players
        [player._set_game(self) for player in self.players]

        # turn and pass count
        self.__turn = 0
        self.__pass_count = 0

        return

    def next(self):
        self.__next__()
        return

    def undo(self) -> bool:
        return self.__reversi.undo()

    def __pass_turn(self) -> None:
        self.__turn = (self.__turn + 1) % 2
        self.__pass_count += 1
        return

    def __put_disc(self) -> None:
        done = False

        while not done:
            done = True

            if not self.__reversi.put_disc(
                self.__players[self.__turn].__input__(),
                self.__turn == 0,
            ):  done = False
            if not done: print("Try again.")

            continue

        self.__pass_count = 0
        self.__pass_turn()
        return

    def __cal_result(self) -> tuple[int, int] | None:
        board = self.get_board()
        result: tuple[int, ...] | tuple[int, int] = tuple(
            sum([
                d.id == target_id
                for d in board
            ])
            for target_id in (DISC_ID[True], DISC_ID[False])
        )
        return result

    def __next__(self) -> bool:
        print(self.get_board())
        print("Black: {}, White: {}".format(*self.__cal_result()))
        print(f"{"Black" if self.__turn == 0 else "White"} turn.")
        """ next player process and """
        if len(self.possible_poss) == 0:
            print(f"Pass")
            self.__pass_turn()
            ...
        else:
            self.__put_disc()
            ...
        if not self.__pass_count > 2: return False
        print("Black: {}, White: {}".format(*self.__cal_result()))
        return True

    def __repr__(self):
        return self.get_board().__repr__()

    def get_board(self):
        return self.__reversi.get_board()

    ...
