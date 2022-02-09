from discord.ext import commands
class PointsSystem(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def points(self,ctx):
    await ctx.send('0 points')


def setup(bot):
  bot.add_cog(PointsSystem(bot))


""" 
PointsSystem:
  Users gain points for doing various things in the discord server.
  How to gain points:
    [2]Send text messages
    [3]Send images
    [5]Send gif/videos
    [1]Add reactions
    [.1/min]Connected to voice channel - alone
    [.2/min]Connected to voice channel - not alone
    Use PogBot commands:
      [2]song played
      
 """
