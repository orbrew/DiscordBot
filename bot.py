import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True

# set prefix for bot to interpret commands
bot = commands.Bot(command_prefix= '!', case_insensitive=True, intents = intents)

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

# load .py files from ./cogs
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ.get('TOKEN'))
