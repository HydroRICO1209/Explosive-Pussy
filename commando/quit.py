from discord.ext import commands
import discord
from progress.match import *
from progress.playerlist import *

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['leave'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def quit(self, ctx):
        dbfunc = self.bot.database_handler
        userid = ctx.author.id
        username = ctx.author.name
        cid = ctx.channel.id
        match = await Match(ctx)
        playerlist = await Playerlist(ctx)
        
        created = await self.bot.db.fetch('SELECT * FROM match WHERE matchid = $1', cid)
        
        if created == []:
            await ctx.send(f'**{username}**, game has not been created')
        else:
            #host
            if userid == match['matchhostid']:
                await ctx.send(f'**{username}**, you do know `ep stop` exist for some reason?')
            else:
                #is member
                if userid in playerlist['player_list']:
                    await dbfunc.setStrValue('player1id', 'playerlist', cid, 1, 'matchid')
                    await self.bot.db.execute('''
DELETE FROM playercard WHERE playerid = $1
''',userid)
                    await ctx.send(f'**{username}**, you had left the game successfully')
                else:
                    #troller
                    await ctx.send(f'**{username}**, you are not in the game')

async def setup(bot):
    await bot.add_cog(MyCog(bot))