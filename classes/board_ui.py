import discord
import random

from .board import Board
from .board_button import BoardButton
from .quit_button import QuitButton

class BoardUI(Board, discord.ui.View):
    def __init__(self, player1, player2):
        Board.__init__(self)
        discord.ui.View.__init__(self)
        super().__init__()
        self.player1 = player1 if random.randint(0, 1) == 0 else player2
        self.player2 = player2 if self.player1 == player1 else player1
        self.turn = 1

        for i in range(1, 8):
            self.add_item(BoardButton(i))
            
        self.add_item(QuitButton())
        
        self.embed = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        self.create_embed(f"{self.player1} starts first!")
    
    def get_embed(self):
        return self.embed
    
    def create_embed(self, message):
        string = (
            f"——————————————\n\n" +
            self.to_string() +
            "\n——————————————\n" +
            f"Turn: {self.turn}\n\n" +
            message
        )
                                    
        self.embed.clear_fields()
        self.embed.add_field(name="", value=string)
    
    async def shutdown(self, interaction):
        self.clear_items()
        self.stop()