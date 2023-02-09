import discord, os, random, asyncio, discord.ext.commands, asyncpg
from discord.ext import commands
from progress.database import Database

intents = discord.Intents.all()
intents.members = True
prefixxx  = ['ep ', 'Ep ', 'eP ', 'EP ']
bot = commands.Bot(command_prefix = prefixxx, case_insensitive=True, activity=discord.Game(name="ep help"),intents=intents)

#######################################################################################MAIN_CODE#######################################################################################
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
bot.remove_command('help')

discord.utils.setup_logging()
@bot.event
async def setup_hook() -> None:
    bot.db: asyncpg.Pool = await asyncpg.create_pool(os.getenv('DATABASE_URL'))
    bot.database_handler = Database(bot)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'**{ctx.author.name}**, this command doesnt exist, check your spellling maybe??')

async def main():
    async with bot:
        [await bot.load_extension(f"commando.{file[:-3]}") for file in os.listdir("commando/") if file.endswith(".py")]
        await bot.start(os.getenv('TOKEN'))

asyncio.run(main())