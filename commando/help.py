from discord.ext import commands
import discord


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def help(self, ctx):
        await ctx.send('''
__Before Game__
ep create - create game (gg)
ep join - join game (gg)
ep quit - quit game (gg)
ep start - start game (gg)
ep stop - stop game (gg)

__During Game__
ep play - play card (gg)
ep draw - draw card (gg)
ep hand - show player's hand (gg)

__Misc__
ep rule - rules (gg)
''')


async def setup(bot):
    await bot.add_cog(help(bot))