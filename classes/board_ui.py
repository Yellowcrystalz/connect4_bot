import discord

from .board_button import BoardButton
from .quit_button import QuitButton

class BoardUI(discord.ui.View):
    def __init__(self, player1, player2):
        super().__init__()
        self.grid = [[] for _ in range(7)]
        self.player1 = player1
        self.player2 = player2
        self.turn = 1

        for i in range(1, 8):
            self.add_item(BoardButton(i))
            
        self.add_item(QuitButton())
    
    async def check_turn(self, interaction):
        if interaction.user != self.player1 and interaction.user != self.player2:
            return True
        elif self.turn % 2 == 1 and interaction.user != self.player1 or self.turn % 2 == 0 and interaction.user != self.player2:
            await interaction.response.send_message(f"{interaction.user.mention} it isn't your turn!", ephemeral=True)
            return True
        
        return False
    
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
                        string_grid += ':yellow_square: '
                except IndexError:
                    string_grid += ':white_square_button: ' 

            string_grid = string_grid[:-1]
            string_grid += '\n'
        
        return string_grid