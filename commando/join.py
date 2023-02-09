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
            match = await Match(ctx)
            playerlist = await Playerlist(ctx)
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            cid = ctx.channel.id
            has_joined = False
            
            #game started/ joined
            if playerlist['player1id'] == None:
                await ctx.send(f'**{username}**, game has not been created.')
            elif userid in (playerlist['player1id'], playerlist['player2id'], playerlist['player3id'], playerlist['player4id']):
                await ctx.send(f'**{username}**, you are already in there')
            elif match['matchstarted'] == True:
                await ctx.send(f'Too late **{username}**, game started')

            #find empty seat
            elif playerlist['player2id'] == 1:
                await dbfunc.setIntValue('player2id', 'playerlist', cid, userid, 'matchid')
                has_joined = True
            elif playerlist['player3id'] == 1:
                await dbfunc.setIntValue('player3id', 'playerlist', cid, userid, 'matchid')
                has_joined = True
            elif playerlist['player4id'] == 1:
                await dbfunc.setIntValue('player4id', 'playerlist', cid, userid, 'matchid')
                has_joined = True
            else:
                await ctx.send(f'**{username}**, the game is full')
            
            if has_joined == True:
                await self.bot.db.execute('''
INSERT INTO playercard (playerid, card1, card2, card3)
VALUES ($1, 'rip bozo', 'rip bozo', 'rip bozo')
''',userid)
                await ctx.send(f'**{username}** joined')
                
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(join(bot))