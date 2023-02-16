from discord.ext import commands
import discord
from progress.match import *
from progress.playerlist import *

class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def create(self, ctx):
        match = await Match(ctx)
        playerlist = await Playerlist(ctx)
        
        username = ctx.author.name
        userid = ctx.author.id
        cid = ctx.channel.id
        created = await self.bot.db.fetch('SELECT * FROM match WHERE matchid = $1', (cid))

        if created == []:
            hehe = ['rip', 'bozo']
            #deck table
            await self.bot.db.execute('''
INSERT INTO deck (matchid, cardlist)
VALUES ($1, $2)
''',cid, hehe)
            
            #match table
            await self.bot.db.execute('''
INSERT INTO match (matchid, matchhostid, matchstarted, matchtotalplayer)
VALUES ($1, $2, False, 1)
''',cid, userid)
            
            #playercard table
            await self.bot.db.execute('''
INSERT INTO playercard (playerid, player_cardlist)
VALUES ($1, $2)
''',userid, hehe)
            
            userid_list = [userid, 0, 0, 0]
            #playerlist table
            await self.bot.db.execute('''
INSERT INTO playerlist (matchid, player_list)
VALUES ($1, $2)
''',cid, userid_list)
            
            await ctx.send(f'Successfully created a room by **{username}**')

        else:
            await ctx.send(f'**{username}**, Game has already been created')


async def setup(bot):
    await bot.add_cog(create(bot))