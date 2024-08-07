import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def play(ctx):
    grid = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
    grid.add_field(name="", value=":black_large_square:")
    await ctx.send(embed=grid)

bot.run(token)