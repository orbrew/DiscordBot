from discord.ext import commands

class TextResponse(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot online')

  @commands.command()
  async def pog(self,ctx):
    await ctx.send('Pog!')

def setup(client):
  client.add_cog(TextResponse(client))
