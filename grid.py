class Coord:
    """docstring for Coord"""
    def __init__(self, x, y):
        self.col = x
        self.row = y
        
    def add(self, other):
        return Coord(self.col + other.col, self.row + other.row)

    def equals(self, other):
        return self.row == other.row and self.col == other.col

    def __str__(self):
        return 'row: ' + str(self.row) + ', col: ' + str(self.col)

class Grid:
    """docstring for Grid"""
    def __init__(self, width, height):
        super(Grid, self).__init__()
        self.width = width
        self.height = height
        self.curr = None
        self.grid = [[' ' for col in range(width)] for row in range(height)]
        self.placed = [[' ' for col in range(width)] for row in range(height)]


    def set_current(self, tetrimino):
        self.curr = tetrimino

    def place_current(self, next):
        for offset in self.curr.cubes:
            cube_pos = self.curr.pos.add(offset)
            self.placed[cube_pos.row][cube_pos.col] = self.curr.char
        self.curr = next

    def clear_lines(self):
        i = len(self.placed)-1
        while i >= 0:
            if ' ' not in self.placed[i]:
                j = i
                while j > 0:
                    self.placed[j] = self.placed[j - 1]
                    j -= 1

                i += 1

            i -= 1


    def get_grid(self):
        return self.grid

    def refresh(self):
        self.grid = [[' ' for col in range(self.width)] for row in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = self.placed[row][col]
        # for cube in self.placed:
        #     self.grid[cube.pos.row][cube.pos.col] = self.curr.char
        for offset in self.curr.cubes:
            cube = self.curr.pos.add(offset)
            self.grid[cube.row][cube.col] = self.curr.char

    def rotate_kick(self):
        x_oob = set()
        y_oob = set()
        for offset in self.curr.cubes:
            cube_pos = self.curr.pos.add(offset)
            if cube_pos.col >= self.width or cube_pos.col < 0 or cube_pos.row >= self.height or cube_pos.row < 0:
                if cube_pos.col >= self.width or cube_pos.col < 0:
                    x_oob.add(offset.col)
                if cube_pos.row >= self.height or cube_pos.row < 0:
                    y_oob.add(offset.row)
            elif self.placed[cube_pos.row][cube_pos.col] != ' ':
                x_oob.add(offset.col)
                y_oob.add(offset.row)

        if 1 in x_oob and self.piece_can_move(Coord(-1, 0)):
            return Coord(-1, 0)
        elif -1 in x_oob and self.piece_can_move(Coord(1, 0)):
            return Coord(1, 0)
        elif 1 in y_oob and self.piece_can_move(Coord(0, -1)):
            return Coord(0, -1)

        return Coord(0, 0)


    def piece_can_move(self, move):
        moved_pos = self.curr.pos.add(move)

        for offset in self.curr.cubes:
            cube_pos = moved_pos.add(offset)

            # Check if inside of grid boundaries
            if cube_pos.col >= self.width or cube_pos.col < 0:
                return False
            if cube_pos.row >= self.height or cube_pos.row < 0:
                return False

            # Check if colliding with placed pieces
            if self.placed[cube_pos.row][cube_pos.col] != ' ':
                return False

        return True

    def __str__(self):
        result = 'Height: ' + str(self.height) + ', Width: ' + str(self.width) + '\n'
        for row in self.grid:
            result += '|'
            for char in row:
                result += char

            result += '|\n'

        return result
        
