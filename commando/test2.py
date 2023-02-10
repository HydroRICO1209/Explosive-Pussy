from discord.ext import commands
import discord
from progress.shuffle import shufflestart

class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx):
        if ctx.author.id == 757508305256972338:
            
            await shufflestart(ctx)
            await ctx.send('first try YOOOOOOOOO')
        else:
            await ctx.send('Would you mind fucking off?')
async def setup(bot):
    await bot.add_cog(test2(bot))