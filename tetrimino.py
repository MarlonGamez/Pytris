import enum
from grid import Grid, Coord

class TPiece(enum.Enum):
    I = 0
    Q = 1
    J = 2
    L = 3
    S = 4
    Z = 5
    T = 6

class Tetrimino:
    """docstring for ClassName"""
    def __init__(self, kind, pos=Coord(5,1)):
        self.kind = kind
        self.pos = pos
        self.cubes = []

        if kind == TPiece.I:
            self.cubes = [Coord(-1, 0), Coord(0, 0), Coord(1, 0), Coord(2, 0)]
        if kind == TPiece.Q:
            self.cubes = [Coord(0, 0), Coord(1, 0), Coord(0, -1), Coord(1, -1)]
        if kind == TPiece.J:
            self.cubes = [Coord(0, 0), Coord(-1, 0), Coord(-1, 1), Coord(1, 0)]
        if kind == TPiece.L:
            self.cubes = [Coord(0, 0), Coord(-1, 0), Coord(1, -1), Coord(1, 0)]
        if kind == TPiece.S:
            self.cubes = [Coord(0, 0), Coord(-1, 0), Coord(0, -1), Coord(1, -1)]
        if kind == TPiece.Z:
            self.cubes = [Coord(0, 0), Coord(1, 0),  Coord(0, 1), Coord(-1, 1)]
        if kind == TPiece.T:
            self.cubes = [Coord(0, 0), Coord(-1, 0), Coord(1, 0), Coord(0, -1)]

    def equals(self, other):
        return self.kind == other.kind

    def move(self, dir):
        return self.pos.add(dir)

    def rotate(self, dir=0):
        if self.kind == TPiece.Q:
            return

        for i in range(4):
            curr = self.cubes[i]
            if dir == 1:
                # rotate clockwise
                self.cubes[i] = Coord(curr.row * -1, curr.col)
            else:
                # rotate counter clockwise
                self.cubes[i] = Coord(curr.row, curr.col * -1)

        

def main():
    test_rotate()

def test_rotate():
    grid = Grid(5, 5)
    print(grid)

    curr = Tetrimino(TPiece.T, Coord(1, 1))
    grid.set_current(curr)
    grid.refresh()
    print(grid)
    print(curr.pos)

    curr.rotate(1)
    grid.refresh()
    print(grid)

    curr.rotate(1)
    grid.refresh()
    print(grid)

    curr.rotate()
    grid.refresh()
    print(grid)

if __name__ == '__main__':
    main()