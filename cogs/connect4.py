import discord
from discord import app_commands
from discord.ext import commands

from classes.accept_ui import AcceptUI
from classes.board_ui import BoardUI


class Connect4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_players = list()
        self.reaction_emojis = [
            chr(0x30 + i) + '\uFE0F\u20E3' for i in range(1, 8)
        ]

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @app_commands.command(name="play", description="Starts a game of Connect 4")
    @app_commands.describe(opponent="Your opponent")
    async def play(self, interaction: discord.Interaction, opponent: discord.Member = None):

        if interaction.user in self.active_players:
            await interaction.response.send_message(
                f"{interaction.user.mention}, you are already in a game!",
                ephemeral=True
            )
            return

        if opponent in self.active_players:
            await interaction.response.send_message(
                f"{opponent.mention} is already in a game!",
                ephemeral=True
            )
            return
        elif opponent is None:
            await interaction.response.send_message(
                f"{interaction.user.mention} sorry we have not implemented single player yet!",
                ephemeral=True
            )
            return

        self.active_players.append(interaction.user)
        self.active_players.append(opponent)

        accept_ui = AcceptUI(interaction.user, opponent)
        await accept_ui.start(interaction)
        await accept_ui.wait()

        if accept_ui.get_response():
            board_ui = BoardUI(interaction.user, opponent)
            await board_ui.start(interaction)
            await board_ui.wait()

        self.active_players.remove(interaction.user)
        self.active_players.remove(opponent)


async def setup(bot):
    await bot.add_cog(Connect4(bot))
