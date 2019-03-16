from grid import Grid, Coord
from tetrimino import Tetrimino, TPiece
from tetris_queue import TQueue
import random
import sys

def main():
    # argv = [width, height, queue, first]
    grid_width, grid_height, queue_size, first = process_args()

    grid = Grid(grid_width, grid_height)
    current = Tetrimino(first, Coord(grid_width//2, 1))
    grid.set_current(current)
    tqueue = TQueue(queue_size)
    hold = None
    

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
            grid.curr.rotate(1)
            move = grid.rotate_kick()
        elif cmd == 'q':
            grid.curr.rotate(0)
            move = grid.rotate_kick()
        else:
            break

        can_move = grid.piece_can_move(move)
        if can_move:
            grid.curr.move(move)
        elif not can_move and move.equals(Coord(0, 1)):
            grid.place_current(tqueue.get())

            # move_in_bounds(grid, grid.curr)



        grid.refresh()
        print(grid)

def process_args():
    args = {arg.split('=')[0].strip().lower():int(arg.split('=')[1].strip()) for arg in sys.argv[1:]}

    grid_width = 10
    grid_height = 22
    queue_size = 4
    first = random.choice(list(TPiece))

    if 'first' in args:
        first = TPiece(args['first'])
    if 'width' in args:
        grid_width = args['width']
    if 'height' in args:
        grid_height = args['height']
    if 'queue' in args:
        queue_size = args['queue']

    return grid_width, grid_height, queue_size, first


def move_in_bounds(grid, piece):
    in_bound, move = grid.piece_can_move(piece, piece.pos)
    while not in_bound:
        piece.pos = piece.move(move)

        in_bound, move = grid.piece_can_move(piece, piece.pos)





if __name__ == '__main__':
    main()