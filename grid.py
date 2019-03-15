class Coord:
    """docstring for Coord"""
    def __init__(self, x, y):
        self.col = x
        self.row = y
        
    def add(self, other):
        return Coord(self.col + other.col, self.row + other.row)

    def __str__(self):
        return 'row: ' + str(self.row) + ', col: ' + str(self.col)

class Grid:
    """docstring for Grid"""
    def __init__(self, width=10, height=22):
        super(Grid, self).__init__()
        self.width = width
        self.height = height
        self.curr = None
        self.grid = [[' ' for col in range(width)] for row in range(height)]


    def set_current(self, tetrimino):
        self.curr = tetrimino

    def get_grid(self):
        return self.grid

    def refresh(self):
        self.grid = [[' ' for col in range(self.width)] for row in range(self.height)]
        for offset in self.curr.cubes:
            cube = self.curr.pos.add(offset)
            self.grid[cube.row][cube.col] = 'O'

    def isInBound(self, piece, pos):
        in_bound = False
        x_move = 0
        y_move = 0

        for offset in piece.cubes:
            cube = pos.add(offset)
            if cube.col >= self.width:
                x_move = min(x_move, self.width - cube.col - 1)
            elif cube.col < 0:
                x_move = max(x_move, 0 - cube.col)

            if cube.row >= self.height:
                y_move = min(y_move, self.height - cube.row - 1)
            elif cube.row < 0:
                y_move = max(y_move, 0 - cube.row)

        if x_move == 0 and y_move == 0:
            in_bound = True

        return in_bound, Coord(x_move, y_move)

    def __str__(self):
        result = 'Height: ' + str(self.height) + ', Width: ' + str(self.width) + '\n'
        for row in self.grid:
            result += '|'
            for char in row:
                result += char

            result += '|\n'

        return result
        
