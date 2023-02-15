from discord.ext import commands
import discord
from progress.match import *
from progress.playerlist import *

class stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def stop(self, ctx):
        playerlist = await Playerlist(ctx)
        match = await Match(ctx)
        userid = ctx.author.id
        username = ctx.author.name
        cid = ctx.channel.id
        
        if match['matchhostid'] == None:
            await ctx.send(f'**{username}**, game has not been created.')
        elif match['matchhostid'] == userid:
            #match table
            await self.bot.db.execute('''
DELETE FROM match
WHERE matchid = $1
''',cid)

            #deck table
            await self.bot.db.execute('''
DELETE FROM deck
WHERE matchid = $1
''',cid)


            #playercard table
            p1 = playerlist['player_list'][0]
            p2 = playerlist['player_list'][1]
            p3 = playerlist['player_list'][2]
            p4 = playerlist['player_list'][3]
            
            if match['matchtotalplayer'] >= 1:
                await self.bot.db.execute('''
DELETE FROM playercard
WHERE playerid = $1
''',p1)
                if match['matchtotalplayer'] >= 2:
                    await self.bot.db.execute('''
DELETE FROM playercard
WHERE playerid = $1
''',p2)
                    if match['matchtotalplayer'] >= 3:
                        await self.bot.db.execute('''
DELETE FROM playercard
WHERE playerid = $1
''',p3)
                        if match['matchtotalplayer'] >= 4:
                            await self.bot.db.execute('''
DELETE FROM playercard
WHERE playerid = $1
''',p4)
                            
                #playerlist table
                await self.bot.db.execute('''
DELETE FROM playerlist
WHERE matchid = $1
''',cid)
                            
            await ctx.send(f'Game stopped by **{username}**')
        else:
            await ctx.send(f'**{username}**, you are not the host')

async def setup(bot):
    await bot.add_cog(stop(bot))