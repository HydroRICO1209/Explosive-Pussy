async def Mobdrop(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    pogchop = await dbfunc.fetchValue('pogchop', 'mobdrop', userid)
    cooked_pogchop = await dbfunc.fetchValue('cooked_pogchop', 'mobdrop', userid)
    beef = await dbfunc.fetchValue('beef', 'mobdrop', userid)
    steak = await dbfunc.fetchValue('steak', 'mobdrop', userid)
    wool = await dbfunc.fetchValue('wool', 'mobdrop', userid)
    map_scrap = await dbfunc.fetchValue('map_scrap', 'mobdrop', userid)
    map = await dbfunc.fetchValue('map', 'mobdrop', userid)
    wither_skull = await dbfunc.fetchValue('wither_skull', 'mobdrop', userid)
    blaze_rod = await dbfunc.fetchValue('blaze_rod', 'mobdrop', userid)
    blaze_powder = await dbfunc.fetchValue('blaze_powder', 'mobdrop', userid)
    ender_pearl = await dbfunc.fetchValue('ender_pearl', 'mobdrop', userid)
    eye_of_ender = await dbfunc.fetchValue('eye_of_ender', 'mobdrop', userid)
    
    misc = {
        'pogchop': pogchop,
        'cooked_pogchop': cooked_pogchop,
        'beef': beef,
        'steak': steak,
        'wool': wool,
        'map_scrap': map_scrap,
        'map': map,
        'wither_skull': wither_skull,
        'blaze_rod': blaze_rod,
        'blaze_powder': blaze_powder,
        'ender_pearl': ender_pearl,
        'eye_of_ender': eye_of_ender
    }