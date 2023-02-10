from discord.ext import commands
import discord
from progress.shuffle import shufflestart
from progress.deck import *
class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        if ctx.author.id == 757508305256972338:
            await shufflestart(ctx)
            deck = await Deck(ctx)
            await ctx.send(f'''
__DECK__
matchid: {deck['matchid']}
card1: {deck['card1']}
card2: {deck['card2']}
card3: {deck['card3']}
card4: {deck['card4']}
card5: {deck['card5']}
card6: {deck['card6']}
card7: {deck['card7']}
card8: {deck['card8']}
''')
        else:
            await ctx.send('Would you mind fucking off?')
async def setup(bot):
    await bot.add_cog(test2(bot))