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

            if match['matchhostid'] == userid and match['matchstarted'] == False and match['matchtotalplayer'] > 1:
                await dbfunc.setBoolValue('matchstarted', match, cid, True, 'matchid')
                await shufflestart(ctx)
                await ctx.send(f"<@{userid}>'s match has started")
            elif match['matchhostid'] != userid: 
                await ctx.send(f'**{username}**, you are not the host')
            elif match['matchhoststarted'] == True: 
                await ctx.send(f'**{username}**, game has already been started')
            elif match['matchtotalplayer'] == 1:
                if userid == 757508305256972338:
                    await ctx.mention('there is only you bruh')
                else:
                    await ctx.send(f'**{username}**, find some friends that doesnt exist?')
            
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(start(bot))