class Farmlist():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.totalslot = await dbfunc.fetchValue('total_slot', 'farmlist', self.userid)
        self.slot1 = await dbfunc.fetchValue('slot1', 'farmlist', self.userid)
        self.slot1time = await dbfunc.fetchValue('slot1time', 'farmlist', self.userid)
        self.slot2 = await dbfunc.fetchValue('slot2', 'farmlist', self.userid)
        self.slot2time = await dbfunc.fetchValue('slot2time', 'farmlist', self.userid)
        self.slot3 = await dbfunc.fetchValue('slot3', 'farmlist', self.userid)
        self.slot3time = await dbfunc.fetchValue('slot3time', 'farmlist', self.userid)
