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
        for cube in self.curr.cubes:
            spot = self.curr.pos.add(cube)
            self.grid[spot.row][spot.col] = 'O'

    def __str__(self):
        result = 'Height: ' + str(self.height) + ', Width: ' + str(self.width) + '\n'
        for row in self.grid:
            result += '|'
            for char in row:
                result += char

            result += '|\n'

        return result
        
