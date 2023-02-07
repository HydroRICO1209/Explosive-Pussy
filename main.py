import discord, os, random, asyncio, discord.ext.commands, asyncpg
from discord.ext import commands
from progress.my_emote import *
from progress.database import Database

intents = discord.Intents.all()
intents.members = True
prefixxx  = ['rpm ', 'Rpm ', 'RPM ', 'RPm ']
bot = commands.Bot(command_prefix = prefixxx, case_insensitive=True, activity=discord.Game(name="rpm start"),intents=intents)

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
async def on_message(message) :
    guild = bot.get_guild(905428951432843304) or bot.fetch_guild(905428951432843304)

    if message.channel.type == discord.ChannelType.private:
        return
    if message.channel.id == 970895283250675813 :
        member = message.mentions[0]
        if not isinstance(member, discord.Member):
            member = await guild.fetch_member(member.id)
        db[f'{member.id}steak'] += 5
        db[f'{member.id}rare_chest'] += 1
        db[f'{member.id}voteCount'] += 1

        voteCount = db[f'{member.id}voteCount']
        if voteCount < 10:
            role = message.guild.get_role(971310924478705695)
        elif voteCount < 18:
            role = message.guild.get_role(971310601668288512)
        elif voteCount < 69:
            role = message.guild.get_role(971311031555072020)
        elif voteCount < 100:
            role = message.guild.get_role(971311323658977281)
        elif voteCount < 420:
            role = message.guild.get_role(971311024051486742)
        elif voteCount >= 420:
            role = message.guild.get_role(971311028694577162)
        else:
            role = message.guild.get_role(905626727005454457)
        await member.add_roles(role)
    await bot.process_commands(message)

######################################################
#######################COMMANDS#######################
######################################################  



@bot.event
async def on_command_error(ctx, error):
    e = My_emote(ctx)
    if isinstance(error, commands.CommandOnCooldown):
        seccd = round(error.cooldown.get_retry_after())
        mincd = 0
        hrcd = 0
        rseccd = 0
        rmincd = 0

        if seccd > 59:  

            rseccd = int(seccd % 60)
            mincd = int((seccd - rseccd) / 60)
            if mincd > 59:
                rmincd = int(mincd % 60)
                hrcd = int((mincd - rmincd) / 60)
        else:
            rseccd = seccd
        await ctx.send(f'''
Dont spam :/ 
Try again in another **{hrcd}h {rmincd}m {rseccd}s**
''')
    
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f'**{ctx.author.name}**, this command doesnt exist, check your spellling maybe??')
    elif isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.name == 'open':
            await ctx.send(f'**{ctx.author.name}**, what are you trying to open?')
        elif ctx.command.name == 'craft':
            e = My_emote(ctx)
            embed = discord.Embed(
                description= f'''
    {e.ph} `pog helmet` ↦ 50 {e.epogchop} + 50 {e.ecoal}
    {e.pc} `pog chestplate` ↦ 80 {e.epogchop} + 80 {e.ecoal}
    {e.pl} `pog leggings` ↦ 70 {e.epogchop} + 70 {e.ecoal}
    {e.pb} `pog boots` ↦ 40 {e.epogchop} + 40 {e.ecoal}
    {e.ps} `pog sword` ↦ 20 {e.epogchop} + 20 {e.ecoal}
    {e.bs} `beefy sword` ↦ 20 {e.ebeef}
    
    {e.ih} `iron helmet` ↦ 50 {e.eiron}
    {e.ic} `iron chestplate` ↦ 80 {e.eiron}
    {e.il} `iron leggings` ↦ 70 {e.eiron}
    {e.ib} `iron boots` ↦ 40 {e.eiron}
    {e.iis} `iron sword` ↦ 20 {e.eiron}
    
    {e.dh} `diamond helmet` ↦ 40 {e.ediamond}
    {e.dc} `diamond chestplate` ↦ 80 {e.ediamond}
    {e.dl} `diamond leggings` ↦ 70 {e.ediamond}
    {e.db} `diamond boots` ↦  40 {e.ediamond}
    {e.ds} `diamond sword` ↦ 20 {e.ediamond}
    ''',
                color = discord.Color.blue())
            embed.set_author(name= 'Recipes(Page 1)',
            icon_url = ctx.author.avatar.url)
            embed.set_footer(text = 'imagine forgetting recipes')
            await ctx.send(embed=embed)
        elif ctx.command.name == 'trade':
            tradelist = f'''
**__Bob, the Builder__**
~~None~~

**__Wagner, the Blacksmith__**
{e.emerald}emerald -> R

**__Skev, the Lumberjack__**
{e.emerald}emerald -> {e.small_sapling}small_sapling
{e.emerald}emerald -> {e.apple}apple

**__Sarth, the Butcher__**
{e.emerald}emerald -> {e.cooked_pogchop}cooked_pogchop
{e.emerald}emerald -> {e.steak}steak

**__Ashley, the Cleric__**
{e.emerald}emerald -> {e.cleansed_dirt}cleansed_dirt
{e.emerald}emerald -> {e.cleansed_water_bucket}cleansed_water_bucket

**__Greg, the Farmer__**
{e.emerald}emerald -> {e.potato}potato
{e.emerald}emerald -> {e.wheat_seeds}wheat_seeds
{e.emerald}emerald -> {e.carrot}carrot
{e.emerald}emerald -> {e.beetroot_seeds}beetroot_seeds

**__Ryuga, the Shepherd__**
~~None~~
'''
            embed = discord.Embed(
                description = tradelist, 
                color = discord.Color.blue())
            embed.set_author(name= f"{ctx.author.display_name}'s trade(Buy)", 
            icon_url = ctx.author.avatar.url)
            await ctx.send(embed=embed)
        else:
            raise error        
    else:
        raise error

async def main():
    async with bot:
        [await bot.load_extension(f"commando.{file[:-3]}") for file in os.listdir("commando/") if file.endswith(".py")]
        await bot.start(os.getenv('TOKEN'))

asyncio.run(main())