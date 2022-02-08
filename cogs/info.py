from datetime import datetime
from discord import Embed
from discord.ext.commands import command
from discord.ext.commands import Cog


class Info(Cog):

    def __init__(self, client):
        self.client = client

    @command(name="userinfo", aliases=["info", "getinfo"])
    async def user_info(self, ctx):
        target = ctx.author

        embed = Embed(title="User info",
                      timestamp=datetime.utcnow())
        embed.set_thumbnail(url=target.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))
