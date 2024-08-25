import discord

from .board_ui import BoardUI

class AcceptUI(discord.ui.View):
    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.response = False
        self.embed = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        self.embed.add_field(name="", value=f"**{player1.name}** has challenged **{player2.name}** to a connect 4 game. Do you accept?")

    @discord.ui.button(label="yes", style=discord.ButtonStyle.green)
    async def yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.player2:
            await interaction.response.send_message(f"{interaction.user.mention}, you are not being challenged!", ephemeral=True)
            return
        
        self.response = True
        await self.shutdown(interaction)

    @discord.ui.button(label="no", style=discord.ButtonStyle.red)
    async def no(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.player1 and interaction.user != self.player2:
            await interaction.response.send_message(f"{interaction.user.mention}, you are not being challenged!", ephemeral=True)
            return
        
        await self.shutdown(interaction)
       
    async def shutdown(self, interaction):
        self.children[0].disabled = True
        self.children[1].disabled = True
        await interaction.response.edit_message(view=self)
        self.stop()

    def get_embed(self):
        return self.embed
    
    def get_response(self):
        return self.response