from discord.ext import commands
import discord
from progress.shuffle import shufflestart
from progress.deck import *
class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx, arg):
        if ctx.author.id == 757508305256972338:
            dbfunc = self.bot.database_handler
            cid = ctx.channel.id
            userid = ctx.author.id
            NewINT = [1,2,3,4]
            
            await dbfunc.setStrValue('namelist', 'test', cid, NewINT, 'matchid')
            fetch_query = f'SELECT namelist FROM test WHEREmatchid = $1'
            answer = await self.bot.db.fetchval(fetch_query, cid)
            await ctx.send(f'datatype: {type(answer), data: {answer}}')
        else:
            await ctx.send('Would you mind fucking off?')
async def setup(bot):
    await bot.add_cog(test2(bot))