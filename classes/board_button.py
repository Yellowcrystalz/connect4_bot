import discord

class BoardButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=str(label), style=discord.ButtonStyle.grey)
    
    async def callback(self, interaction: discord.Interaction):
        if await self.check_turn(interaction):
            return

        view = self.view

        view.place(int(self.label), 'X' if view.turn % 2 == 1 else 'O')
        view.turn += 1
        string = f"**{view.player1.name if view.turn % 2 == 0 else view.player2.name}** has placed at {self.label}\n"

        terminal = view.check_terminal()
        
        if terminal == -1 or terminal == 1:
            string += f"**{view.player1 if terminal == 1 else view.player2}** has won!"
            await view.shutdown(interaction)
        else:
            string += f"**{view.player1.name if view.turn % 2 == 1 else view.player2.name}** it is your turn"

            if not view.valid_move(int(self.label)):
                view.remove_item(self)

        view.create_embed(string)
        await interaction.response.edit_message(content=f"{view.player1.mention if view.turn % 2 == 1 else view.player2.mention}",
                                                embed=view.get_embed(), 
                                                view=view)
        
    async def check_turn(self, interaction):
        view = self.view

        if interaction.user != view.player1 and interaction.user != view.player2:
            await interaction.response.send_message(f"{interaction.user.mention}, you aren't in this game!", ephemeral=True)
            return True
        elif view.turn % 2 == 1 and interaction.user != view.player1 or view.turn % 2 == 0 and interaction.user != view.player2:
            await interaction.response.send_message(f"{interaction.user.mention}, it isn't your turn!", ephemeral=True)
            return True
        
        return False