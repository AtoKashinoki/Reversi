

from Reversi.Game import Reversi1v1
from Reversi.Players import Human, RandomAI


SIZE = (8, 8)


def main():
    reversi = Reversi1v1((RandomAI(), RandomAI()))
    done = False
    while not done:
        done = next(reversi)
        continue
    input()
    return


if __name__ == '__main__':
    main()
    ...
