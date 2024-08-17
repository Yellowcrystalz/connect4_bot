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

        for i in range(6):
            for j in range(7):
                try:
                    if self.grid[j][5 - i] == 'X':
                        string_grid += ':red_square: '
                    else:
                        string_grid += ':blue_square: '
                except IndexError:
                    string_grid += ':white_square_button: ' 

            string_grid = string_grid[:-1]
            string_grid += '\n'
        
        return string_grid