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
            
            p1 = playerlist['player1id']
            p2 = playerlist['player2id']
            p3 = playerlist['player3id']
            p4 = playerlist['player4id']

            if match['matchtotalplayer'] >= 1:
                long += f'1) <@{p1}>\n'
                if match['matchtotalplayer'] >= 2:
                    long += f'2) <@{p2}>\n'
                    if match['matchtotalplayer'] >= 3:
                        long += f'3) <@{p3}>\n'
                        if match['matchtotalplayer'] >= 4:
                            long += f'4) <@{p4}>\n'

            embed = discord.Embed(
                description=f'''
Game created by **{username}**
{long}
''',
                color=discord.Color.blue())
            embed.set_author(name='Lobby', icon_url=ctx.author.avatar.url)
            embed.add_field(name='Link', value='[Offcial server](https://discord.gg/ACCYFpPYAj)')
            embed.set_footer(text='Go grab some drinks')
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(join(bot))