class Board():
    def __init__(self):
        self.grid = [[] for _ in range(7)]

    def valid_move(self, position):
        if position > 7:
            return False

        return len(self.grid[position - 1]) < 6
    
    def place(self, position, player):
        if not self.valid_move(position):
            return False
        
        self.grid[position - 1].append(player)
    
    def to_string(self):
        string_grid = ""

        for j in range(6):
            for i in range(7):
                try:
                    if self.grid[i][5 - j] == 'X':
                        string_grid += ':red_square: '
                    else:
                        string_grid += ':yellow_square: '
                except IndexError:
                    string_grid += ':white_square_button: ' 

            string_grid = string_grid[:-1]
            string_grid += '\n'

        return string_grid
    
    def check_terminal(self):
        for j in range(6):
            blank_count = 0

            for i in range(7):

                try:
                    symbol = self.grid[i][j]

                    if i < 4 and j < 3:
                        pass

                    if i < 4:
                       if self.check_horizontal(i, j, symbol):
                            return 1 if symbol == 'X' else -1
                    
                    if j < 3:
                        if self.check_vertical(i, j, symbol):
                            return 1 if symbol == 'X' else -1
                    
                    if self.check_diagonal(i, j, symbol):
                        return 1 if symbol == 'X' else -1

                except IndexError:
                    blank_count += 1
                    
            if blank_count == 7:
                return 0
    
    def check_horizontal(self, i, j, symbol):
        try:
            if (
                self.grid[i + 1][j] == symbol and
                self.grid[i + 2][j] == symbol and
                self.grid[i + 3][j] == symbol
            ):
                return True
        except IndexError:
            return False
        
        return False
    
    def check_vertical(self, i, j, symbol):
        try:
            if (
                self.grid[i][j + 1] == symbol and
                self.grid[i][j + 2] == symbol and
                self.grid[i][j + 3] == symbol
            ):
                return True
        except IndexError:
            return False
        
        return False
    
    def check_diagonal(self, i, j, symbol):
        if self.check_bottom_right_to_top_left(i, j, symbol):
            return True
        elif self.check_bottom_left_to_top_right(i, j, symbol):
            return True
        return False
    
    def check_bottom_right_to_top_left(self, i, j, symbol):
        try:
            if (
                self.grid[i - 1][j + 1] == symbol and
                self.grid[i - 2][j + 2] == symbol and
                self.grid[i - 3][j + 3] == symbol
            ):
                return True
        except IndexError:
            return False
        
        return False           
    
    def check_bottom_left_to_top_right(self, i, j, symbol):
        try:
            if (
                self.grid[i + 1][j + 1] == symbol and
                self.grid[i + 2][j + 2] == symbol and
                self.grid[i + 3][j + 3] == symbol
            ):
                return True
        except IndexError:
            return False
        
        return False