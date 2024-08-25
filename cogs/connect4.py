import discord
from discord import app_commands
from discord.ext import commands

from classes.accept_ui import AcceptUI
from classes.board_ui import BoardUI

class Connect4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_players = list()
        self.reaction_emojis = [chr(0x30 + i) + '\uFE0F\u20E3' for i in range(1, 8)]
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @app_commands.command(name="play", description="Starts a game of Connect 4")
    @app_commands.describe(opponent="Your opponent")
    async def play(self, interaction: discord.Interaction, opponent: discord.Member = None):
        if opponent == None:
            await interaction.response.send_message(f"{interaction.user.mention} sorry we have not implemented single player yet!", ephemeral=True)
            return

        accept_ui = AcceptUI(interaction.user, opponent)
        await accept_ui.start(interaction)
        await accept_ui.wait()

        if accept_ui.get_response():
            board_ui = BoardUI(interaction.user, opponent)
            await board_ui.start(interaction)

async def setup(bot):
    await bot.add_cog(Connect4(bot))