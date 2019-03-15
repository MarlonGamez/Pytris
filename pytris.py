from grid import Grid
from tetrimino import Tetrimino, Coord, TPiece

def main():

    current = Tetrimino(TPiece.Q)
    grid = Grid()
    grid.set_current(current)
    grid.refresh()
    print(grid)

    while True:
        cmd = input()

        if cmd == 'a':
            move = Coord(-1, 0)
        elif cmd == 'd':
            move = Coord(1, 0)
        elif cmd == 's':
            move = Coord(0, 1)
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