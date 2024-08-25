import discord

class BoardButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=str(label), style=discord.ButtonStyle.grey)
    
    async def callback(self, interaction: discord.Interaction):
        if await self.check_turn(interaction):
            return

        self.view.place(int(self.label), 'X' if self.view.turn % 2 == 1 else 'O')
        self.view.turn += 1
        string = f"**{self.view.player1.name if self.view.turn % 2 == 0 else self.view.player2.name}** has placed at {self.label}\n"

        terminal = self.view.check_terminal()
        
        if terminal == -1 or terminal == 1:
            string += f"{self.view.player1 if terminal == 1 else self.view.player2} has won!"
            await self.view.shutdown(interaction)
        else:
            if not self.view.valid_move(int(self.label)):
                self.view.remove_item(self)

            string += f"**{self.view.player1.name if self.view.turn % 2 == 1 else self.view.player2.name}** it is your turn"

        self.view.create_embed(string)
        await interaction.response.edit_message(content=f"{self.view.player1.mention if self.view.turn % 2 == 1 else self.view.player2.mention}",
                                                embed=self.view.get_embed(), 
                                                view=self.view)
        
    async def check_turn(self, interaction):
        if interaction.user != self.view.player1 and interaction.user != self.view.player2:
            await interaction.response.send_message(f"{interaction.user.mention}, you aren't in this game!", ephemeral=True)
            return True
        elif self.view.turn % 2 == 1 and interaction.user != self.view.player1 or self.view.turn % 2 == 0 and interaction.user != self.view.player2:
            await interaction.response.send_message(f"{interaction.user.mention}, it isn't your turn!", ephemeral=True)
            return True
        
        return False