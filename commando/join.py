from discord.ext import commands
import discord
from progress.match import *
from progress.playerlist import *

class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def join(self, ctx):
        try:
            match = Match(ctx)
            playerlist = Playerlist(ctx)
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            cid = ctx.channel.id
            
            #game started/ joined
            if userid in (playerlist['player1id'], playerlist['player2id'], playerlist['player3id'], playerlist['player4id']):
                await ctx.send(f'{username}, you are already in there')
            elif match['matchstarted'] == True:
                await ctx.send(f'Too late {username}, game started')

            #find empty seat
            elif player2id == 0:
                await dbfunc.setIntValue('player2id', 'playerlist', cid, userid, 'matchid')
                await ctx.send(f'{username}joined')
            elif player3id == 0:
                await dbfunc.setIntValue('player3id', 'playerlist', cid, userid, 'matchid')
                await ctx.send(f'{username}joined')
            elif player4id == 0:
                await dbfunc.setIntValue('player4id', 'playerlist', cid, userid, 'matchid')
                await ctx.send(f'{username}joined')
            else:
                await ctx.send(f'{username}, the game is full')
            
            
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(join(bot))