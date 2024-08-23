import discord
from discord import app_commands
from discord.ext import commands
import asyncio

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
        # if interaction.user.id in self.active_players:
        #     await interaction.response.send_message("Bruh you are already in a game")
        #     return
        
        # if opponent == None:
        #     await interaction.response.send_message(f"Do you want to play a single-player(AI) or multi-player game?")
        #     return
        # elif opponent.id == interaction.user.id:
        #     await interaction.response.send_message(f"You can't play yourself :face_with_raised_eyebrow:")
        #     return
        # elif opponent.id in self.active_players:
        #     await interaction.response.send_message(f"{opponent.name} is already in a game")
        #     return
        
        # self.active_players.append(interaction.user.id)
        # self.active_players.append(opponent.id)

        # embedded_msg = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        # embedded_msg.add_field(name="", value=f"{interaction.user.name} has challeneged {opponent.name} to a connect 4 game. Do you accept? {opponent.mention}")
        # await interaction.response.send_message(embed=embedded_msg)

        # await interaction.response.send_message(f"The game has started!")
        # asyncio.create_task(self.game_two_player(interaction))
        # embedded_msg = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        # embedded_msg.add_field(name="", value=board.to_string())

        board = BoardUI(interaction.user, opponent)
        await interaction.response.send_message(view=board)

    async def game_two_player(self, interaction):
        board = BoardUI()
        message = await self.display_board(interaction, board)

        def check(reaction, user):
            return user == interaction.user and reaction.message.id == message.id and str(reaction.emoji) in self.reaction_emojis
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            await interaction.followup.send(f"{user.display_name} reacted with {reaction.emoji}")
        except asyncio.TimeoutError:
            await interaction.followup.send("Timeout")
        
        for i in range(1,8):
            if reaction.emoji == (chr(0x30 + i) + '\uFE0F\u20E3'):
                board.place(i, 'X')

        message = await self.display_board(interaction, board)
    
async def setup(bot):
    await bot.add_cog(Connect4(bot))