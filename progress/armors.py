async def Armors(self, ctx):
    dbfunc = bot.database_handler

    userid = ctx.author.id
    helmet = await dbfunc.fetchValue('helmet', 'armors', userid)
    chestplate = await dbfunc.fetchValue('chestplate', 'armors', userid)
    leggings = await dbfunc.fetchValue('leggings', 'armors', userid)
    boots = await dbfunc.fetchValue('boots', 'armors', userid)
    sword = await dbfunc.fetchValue('sword', 'armors', userid)
    