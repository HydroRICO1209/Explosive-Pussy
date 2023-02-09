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
            #deck table
            await self.bot.db.execute('''
INSERT INTO deck (matchid, card1, card2, card3, card4, card5, card6, card7, card8)
VALUES ($1, 'rip bozo', 'rip bozo', 'rip bozo', 'rip bozo', 'rip bozo', 'rip bozo', 'rip bozo','rip bozo')
''',cid)
            
            #match table
            await self.bot.db.execute('''
INSERT INTO match (matchid, matchhostid, matchstarted, matchtotalplayer)
VALUES ($1, $2, False, 1)
''',cid, userid)
            
            #playercard table
            await self.bot.db.execute('''
INSERT INTO playercard (playerid, card1, card2, card3)
VALUES ($1, 'rip bozo', 'rip bozo', 'rip bozo')
''',userid)

            #playerlist table
            await self.bot.db.execute('''
INSERT INTO playerlist (matchid, player1id, player2id, player3id, player4id)
VALUES ($1, $2, 1, 1, 1)
''',cid, userid)

            await ctx.send(f'Successfully created a room by **{username}**')

            ############################################
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
            embed.add_field(
                name='Link', value='[Offcial server](https://discord.gg/ACCYFpPYAj)')
            embed.set_footer(text='Go grab some drinks')
            await ctx.send(embed=embed)

        else:
            await ctx.send(f'**{username}**, Game has already been created')


async def setup(bot):
    await bot.add_cog(create(bot))