import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import asyncio
from itertools import cycle
# import sys

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')
bot = commands.Bot(command_prefix='c4 ', intents=discord.Intents.all())
bot_statuses = cycle(["Status One", "Status Two"])


@tasks.loop(seconds=5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))


@bot.event
async def on_ready():
    print("Online")
    change_bot_status.start()

    try:
        synced_commands = await bot.tree.sync()
        if len(synced_commands) == 1:
            print("Synced 1 command.")
        else:
            print(f"Synced {len(synced_commands)} commands.")
    except Exception as e:
        print("An error with syncing application commands has occured: ", e)


@bot.command()
@commands.is_owner()
async def kill(ctx):
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

if __name__ == "__main__":
    asyncio.run(main())
