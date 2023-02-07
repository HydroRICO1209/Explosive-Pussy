async def Stats(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    hp = await dbfunc.fetchValue('hp', 'stats', userid)
    highest_area = await dbfunc.fetchValue('highest_area', 'stats', userid)
    atk = await dbfunc.fetchValue('atk', 'stats', userid)
    defend = await dbfunc.fetchValue('defend', 'stats', userid)
    xp = await dbfunc.fetchValue('xp', 'stats', userid)
    level = await dbfunc.fetchValue('level', 'stats', userid)
    maxxp = level * 200
    area = await dbfunc.fetchValue('area', 'stats', userid)
    
    stats = {
        'hp': hp, 
        'highest_area': highest_area, 
        'atk': atk, 
        'defend': defend, 
        'xp': xp, 
        'level': level, 
        'maxxp': maxxp, 
        'area': area        
    }
    
    return stats