from discord.ext import commands
import discord
from progress.match import *
from progress.shuffle import shufflestart

class start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def start(self, ctx):
        try:
            match = await Match(ctx)
            dbfunc = self.bot.database_handler
            username = ctx.author.name
            userid = ctx.author.id
            cid = ctx.channel.id

            if match['matchhostid'] == userid and match['matchstarted'] == False:
                await dbfunc.setBoolValue('matchstarted', match, cid, True, 'matchid')
                await shufflestart(ctx)
                await ctx.send(f"<@{userid}>'s match has started")
            elif match['matchhostid'] != cid:
                await ctx.send(f'**{username}**, you are not the host')
            elif match['matchhoststarted'] == True:
                await ctx.send(f'**{username}**, game has already been started')
                
            
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(start(bot))