import discord
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @commands.command()
    async def play(self, ctx):
        grid = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        grid.add_field(name="", value=":white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:")
        
        message = await ctx.send(embed=grid)

        for i in range(1, 8):
            unicode = chr(0x30 + i) + '\uFE0F\u20E3'
            await message.add_reaction(unicode)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return
        
        if reaction.message.embeds and reaction.message.embeds[0].title == "Yellow's Connect 4":
            await reaction.message.channel.send(f"{user.display_name} reacted with {reaction.emoji}")
            

async def setup(bot):
    await bot.add_cog(Game(bot))