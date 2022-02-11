import discord
from discord import Embed
from discord.ext.commands import command
from discord.ext.commands import Cog
from datetime import datetime


class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="userinfo", aliases=["info", "getinfo", "ui", "user"])
    async def user_info(self, ctx, target: discord.Member = None):
        target = target or ctx.author

        embed = Embed(title="User info",
                      color=target.color,
                      timestamp=datetime.utcnow())
        embed.set_thumbnail(url=target.avatar_url)

        fields = [("Name", str(target), True),
                  ("Top role", target.top_role.mention, True),
                  ("Status", str(target.status).title(), True),
                  ("Activity", target.activity, True),
                  ("ID", target.id, False),
                  ("Joined server", target.joined_at.strftime(
                      "%m/%d/%Y %H:%M:%S"), True),
                  ("Account created", target.created_at.strftime(
                      "%m/%d/%Y %H:%M:%S"), True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @command(name="serverinfo", aliases=["guild", "server", "guildinfo", "gi", "si"])
    async def server_info(self, ctx):
        embed = Embed(title="Server info",
                      timestamp=datetime.utcnow())

        fields = [("ID", ctx.guild.id, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Region", ctx.guild.region, True),
                  ("Created", ctx.guild.created_at.strftime(
                      "%m/%d/%Y %H:%M:%S"), True),
                  ("Members", len(ctx.guild.members), True),
                  ("Text channels", len(ctx.guild.text_channels), True),
                  ("Voice channels", len(ctx.guild.voice_channels), True),
                  ("Roles", ctx.guild.roles, True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @command(name="online")
    async def online_info(self, ctx):
        user_list=[]
        for member in ctx.guild.members:
            if str(member.status) != "Offline":
                user_list.append(member.name)
        await ctx.send(user_list)



def setup(bot):
    bot.add_cog(Info(bot))
