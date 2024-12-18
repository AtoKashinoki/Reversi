

from time import time
from copy import copy, deepcopy
from Reversi.Game import Reversi1v1


SIZE = (8, 8)


if __name__ == '__main__':
    d1 = Reversi1v1(SIZE).get_board().get_data()
    for d in (d1, ):
        s = time()
        for _ in range(10000):
            copy(d)
            continue
        print(time() - s)
        continue
    ...
