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
    grid.add_field(name="", value=":white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:\n:white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button: :white_square_button:")
    
    message = await ctx.send(embed=grid)

    await message.add_reaction('\u0031\uFE0F\u20E3')
    await message.add_reaction('\u0032\uFE0F\u20E3')
    await message.add_reaction('\u0033\uFE0F\u20E3')
    await message.add_reaction('\u0034\uFE0F\u20E3')
    await message.add_reaction('\u0035\uFE0F\u20E3')
    await message.add_reaction('\u0036\uFE0F\u20E3')
    await message.add_reaction('\u0037\uFE0F\u20E3')

bot.run(token)