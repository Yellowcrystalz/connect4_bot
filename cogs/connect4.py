import discord
from discord import app_commands
from discord.ext import commands
import asyncio

from classes.board import Board

class Connect4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = 0
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @app_commands.command(name="play", description="Starts a game of Connect 4")
    async def play(self, interaction: discord.Interaction):
        self.counter += 1 
        await interaction.response.send_message(f"Game {self.counter} has started!")
        asyncio.create_task(self.game(interaction))

    async def game(self, interaction):
        board = Board()
        grid = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        grid.add_field(name="", value=board.to_string())
        
        message = await interaction.followup.send(embed=grid)

        reaction_emojis = [chr(0x30 + i) + '\uFE0F\u20E3' for i in range(1, 8)]

        for emoji in reaction_emojis:
            await message.add_reaction(emoji)

        def check(reaction, user):
            return user == interaction.user and reaction.message.id == message.id and str(reaction.emoji) in reaction_emojis
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            await interaction.followup.send(f"{user.display_name} reacted with {reaction.emoji}")
        except asyncio.TimeoutError:
            await interaction.followup.send("Timeout")
        
        self.counter -= 1
            
async def setup(bot):
    await bot.add_cog(Connect4(bot))