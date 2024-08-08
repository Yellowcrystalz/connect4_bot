import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio


load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Online")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("I am dying")
    await bot.close()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())