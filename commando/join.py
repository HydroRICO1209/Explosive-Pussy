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
        if playerlist['player_list'] == None:
            await ctx.send(f'**{username}**, game has not been created.')
        elif userid in playerlist['player_list']:
            await ctx.send(f'**{username}**, you are already in there')
        elif match['matchstarted'] == True:
            await ctx.send(f'Too late **{username}**, game started')

        #find empty seat
        elif match['matchtotalplayer'] < 4:
            newlist = playerlist['player_list'].append(userid)
            await dbfunc.setStrValue('player_list', 'playerlist', cid, newlist, 'matchid')
            await self.bot.db.execute('''
INSERT INTO playercard (playerid, card1, card2, card3)
VALUES ($1, 'rip bozo', 'rip bozo', 'rip bozo')
''',userid)
            await ctx.send(f'**{username}** joined')
            
            n=1
            for playerid in playerlist['player_list']:
                long += f'{n}) <@{playerid}>\n'
                n+=1
            embed = discord.Embed(
                description=f'''
Game created by **<@{match['matchhostid']}>**
{long}
''',
                color=discord.Color.blue())
            embed.set_author(name='Lobby', icon_url=ctx.author.avatar.url)
            embed.add_field(name='Link', value='[Offcial server](https://discord.gg/ACCYFpPYAj)')
            embed.set_footer(text='Go grab some drinks')
            await ctx.send(embed=embed)
            
        elif len(playerlist['playerlist']) >= 4:
            await ctx.send(f'**{username}**, the game is full')

async def setup(bot):
    await bot.add_cog(join(bot))