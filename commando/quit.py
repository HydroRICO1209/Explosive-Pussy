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
        cid = ctx.channel.id
        match = await Match(ctx)
        playerlist = await Playerlist(ctx)
        
        created = await self.bot.db.fetch('SELECT * FROM match WHERE matchid = $1', (cid))
        await ctx.send(f'created: {created}')
        if created == []:
            await ctx.send(f'**{username}**, game has not been created')
        else:
            if userid == playerlist['player1id']:
                await dbfunc.setIntValue('player1id', 'playerlist', cid, 1, matchid)
                await ctx.send(f'**{username}**, you had left the game successfully')
            elif userid == playerlist['player2id']:
                await dbfunc.setIntValue('player2id', 'playerlist', cid, 1, matchid)
                await ctx.send(f'**{username}**, you had left the game successfully')
            elif userid == playerlist['player3id']:
                await dbfunc.setIntValue('player3id', 'playerlist', cid, 1, matchid)
                await ctx.send(f'**{username}**, you had left the game successfully')
            elif userid == playerlist['player4id']:
                await dbfunc.setIntValue('player4id', 'playerlist', cid, 1, matchid)
                await ctx.send(f'**{username}**, you had left the game successfully')


async def setup(bot):
    await bot.add_cog(MyCog(bot))