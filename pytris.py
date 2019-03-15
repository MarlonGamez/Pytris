from grid import Grid
from tetrimino import Tetrimino, Coord, TPiece
from tetris_queue import TQueue
import random

def main():

    grid = Grid()
    current = Tetrimino(random.choice(list(TPiece)))
    queue = TQueue(4)
    placed = []

    grid.set_current(current)
    grid.refresh()
    print(grid)

    while True:
        cmd = input()
        move = Coord(0, 0)

        if cmd == 'a':
            move = Coord(-1, 0)
        elif cmd == 'd':
            move = Coord(1, 0)
        elif cmd == 's':
            move = Coord(0, 1)
        elif cmd == 'e':
            current.rotate(1)
        elif cmd == 'q':
            current.rotate(0)
        else:
            break

        new_pos = current.move(move)
        if isInBound(new_pos):
            current.pos = new_pos


        grid.refresh()
        print(grid)


def isInBound(tetrimino):
    return True


if __name__ == '__main__':
    main()