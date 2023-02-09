from discord.ext import commands
import discord


class Monkeyballs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def monkeyballs(self, ctx):
        nama = None
        if userid == 564103314673762304:
            nama = 'zyong'
            
        if nama == None:
            await ctx.send(f"lemme guess, its {ctx.author.name}")
        else:
            await ctx.send(f"lemme guess, its {nama}")


async def setup(bot):
    await bot.add_cog(Monkeyballs(bot))