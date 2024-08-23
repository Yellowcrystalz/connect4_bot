import discord

class QuitButton(discord.ui.Button):
    def __init__(self):
       super().__init__(label="Quit", style=discord.ButtonStyle.red)
    
    async def callback(self, interaction:discord.Interaction):
        self.view.clear_items()
        self.view.stop()
        await interaction.response.edit_message(view=self.view)