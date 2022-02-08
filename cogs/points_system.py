from discord.ext import commands

class PointsSystem(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.command()
  async def points(self,ctx):
    await ctx.send('0 points')


def setup(client):
  client.add_cog(PointsSystem(client))


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
