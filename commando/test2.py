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

            fetch_query = f'SELECT fuck FROM test WHERE matchid = $1'
            answer = await self.bot.db.fetchval(fetch_query, cid)
            await ctx.send(f'1)datatype: {type(answer)}, data: {answer}')
            await ctx.send(f'2)datatype: {type(answer[0])}, data: {answer[0]}')
            
            idk = [1234, 2345, 3456]
            await dbfunc.setIntValue('fuck', 'test', cid, idk, 'matchid')
            
            fetch_query = f'SELECT fuck FROM test WHERE matchid = $1'
            answer = await self.bot.db.fetchval(fetch_query, cid)
            await ctx.send(f'3)datatype: {type(answer)}, data: {answer}')
            await ctx.send(f'4)datatype: {type(answer[0])}, data: {answer[0]}, {answer[1]}, {answer[2]}')
        else:
            await ctx.send('Would you mind fucking off?')
async def setup(bot):
    await bot.add_cog(test2(bot))