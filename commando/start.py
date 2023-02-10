from discord.ext import commands
import discord, random
from progress.match import *
from progress.playerlist import *
from progress.deck import *
from progress.shuffle import shufflestart

class start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def start(self, ctx):
        match = await Match(ctx)
        playerlist = await Playerlist(ctx)
        deck = await Deck(ctx)
        dbfunc = self.bot.database_handler
        username = ctx.author.name
        userid = ctx.author.id
        cid = ctx.channel.id

        #started
        if match['matchhostid'] == userid and match['matchstarted'] == False and match['matchtotalplayer'] > 1:
            await dbfunc.setBoolValue('matchstarted', match, cid, True, 'matchid')
            await shufflestart(ctx)
            await ctx.send(f"<@{userid}>'s match has started")
            for player in playerlist:
                has_taken = False
                while has_taken == False:
                    random.randint(1,8)
                
            
        #not started
        elif match['matchhostid'] != userid: 
            await ctx.send(f'**{username}**, you are not the host')
        elif match['matchstarted'] == True: 
            await ctx.send(f'**{username}**, game has already been started')
        elif match['matchtotalplayer'] == 1:
            if userid == 757508305256972338:
                await ctx.send(f'**{username}**, there is only you bruh')
            else:
                await ctx.send(f'**{username}**, find some friends that doesnt exist?')


async def setup(bot):
    await bot.add_cog(start(bot))