from grid import Grid, Coord
from tetrimino import Tetrimino, TPiece
from tetris_queue import TQueue
import random

def main():

    grid = Grid()
    # current = Tetrimino(random.choice(list(TPiece)))
    current = Tetrimino(TPiece.I)
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
        in_bound, _ = grid.isInBound(current, new_pos)
        if in_bound:
            current.pos = new_pos
        else:
            moveInBounds(grid, current)

        grid.refresh()
        print(grid)


def moveInBounds(grid, piece):
    in_bound, move = grid.isInBound(piece, piece.pos)
    while not in_bound:
        piece.pos = piece.move(move)

        in_bound, move = grid.isInBound(piece, piece.pos)





if __name__ == '__main__':
    main()