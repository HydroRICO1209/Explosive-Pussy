class Armors():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.helmet = await dbfunc.fetchValue('helmet', 'armors', self.userid)
        self.chestplate = await dbfunc.fetchValue('chestplate', 'armors', self.userid)
        self.leggings = await dbfunc.fetchValue('leggings', 'armors', self.userid)
        self.boots = await dbfunc.fetchValue('boots', 'armors', self.userid)
        self.sword = await dbfunc.fetchValue('sword', 'armors', self.userid)