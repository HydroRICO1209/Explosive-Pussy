from discord.ext import commands
import discord


class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx, arg):
        if ctx.author.id == 757508305256972338:
            dbfunc = self.bot.database_handler
            cid = ctx.channel.id
            await dbfunc.setIntValue('nombor', 'test', cid, arg, 'matchid')
            await ctx.send(f'db should be {arg} now, or you are fked too')
        else:
            await ctx.send('Would you mind fucking off?')
async def setup(bot):
    await bot.add_cog(test2(bot))