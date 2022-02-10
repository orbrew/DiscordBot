import discord
from discord import Embed
from discord.ext.commands import command
from discord.ext.commands import Cog
from datetime import datetime


class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="userinfo", aliases=["info", "getinfo"])
    async def user_info(self, ctx, target: discord.Member = None):
        target = target

        embed = Embed(title="User info",
                      color=target.color,
                      timestamp=datetime.utcnow())
        embed.set_thumbnail(url=target.avatar_url)
        

        fields = [("Name", str(target), True),
                  ("Top role", target.top_role.mention, True),
                  ("Status", str(target.status).title(), True),
                  ("Activity", target.activity, True),
                  ("Account created", target.created_at.strftime("%m/%d/%Y %H:%M%S"), True),
                  ("Joined server", target.joined_at.strftime("%m/%d/%Y %H:%M:%S"), True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
