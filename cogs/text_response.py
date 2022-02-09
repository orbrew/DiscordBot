import random
from discord.ext.commands import Cog
from discord.ext.commands import command

class TextResponse(Cog):
  def __init__(self,bot):
    self.bot = bot

  @Cog.listener()
  async def on_ready(self):
    print('Bot online')

  @command()
  async def pog(self,ctx):
    await ctx.send('Pog!')

  @command(name="coinflip", aliases=["cf", "flip","coin","ht"])
  async def coinflip(self,ctx):
    result = random.randint(1,2)
    if result == 1:
      result = "Heads"
    else:
      result = "Tails"
    await ctx.send(result)

def setup(bot):
  bot.add_cog(TextResponse(bot))
