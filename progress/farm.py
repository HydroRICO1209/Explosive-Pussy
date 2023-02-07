class Farm():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.small_sapling = await dbfunc.fetchValue('small_sapling', 'farm', self.userid)
        self.medium_sapling = await dbfunc.fetchValue('medium_sapling', 'farm', self.userid)
        self.large_sapling = await dbfunc.fetchValue('large_sapling', 'farm', self.userid)
        self.apple = await dbfunc.fetchValue('apple', 'farm', self.userid)
        self.wheat_seeds = await dbfunc.fetchValue('wheat_seeds', 'farm', self.userid)
        self.wheat = await dbfunc.fetchValue('wheat', 'farm', self.userid)
        self.potato = await dbfunc.fetchValue('potato', 'farm', self.userid)
        self.poisonous_potato = await dbfunc.fetchValue('poisonous_potato', 'farm', self.userid)
        self.carrot = await dbfunc.fetchValue('carrot', 'farm', self.userid)
        self.beetroot_seeds = await dbfunc.fetchValue('beetroot_seeds', 'farm', self.userid)
        self.beetroot = await dbfunc.fetchValue('beetroot', 'farm', self.userid)
        self.cleansed_water_bucket = await dbfunc.fetchValue('cleansed_water_bucket', 'farm', self.userid)
        self.cleansed_dirt = await dbfunc.fetchValue('cleansed_dirt', 'farm', self.userid)