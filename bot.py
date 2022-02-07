import os
from discord.ext import commands

#set prefix for bot to interpret commands
client = commands.Bot(command_prefix= '!')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

#load .py files from ./cogs
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ.get('TOKEN'))
