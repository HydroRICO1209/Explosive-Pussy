from discord.ext import commands
import discord


class monkeyballs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def monkeyballs(self, ctx):
        nama = None
        userid = ctx.author.id
        
        if userid == 564103314673762304:
            nama = 'zyong'
        elif userid == 909299929854398474:
            nama = 'hong ming'
        elif userid == 719081338862567475:
            nama = 'qameel'
        elif userid == 757508305256972338:
            nama = 'juan han'
            
        if nama == None:
            await ctx.send(f"lemme guess, its {ctx.author.name}")
        else:
            await ctx.send(f"lemme guess, its {nama}")


async def setup(bot):
    await bot.add_cog(monkeyballs(bot))