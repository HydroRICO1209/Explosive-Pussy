async def Misc(ctx):
    dbfunc = ctx.bot.database_handler
    
    userid = ctx.author.id
    emerald = await dbfunc.fetchValue('emerald', 'misc', userid)
    cobble = await dbfunc.fetchValue('cobble', 'misc', userid)
    coal = await dbfunc.fetchValue('coal', 'misc', userid)
    iron_ingot = await dbfunc.fetchValue('iron_ingot', 'misc', userid)
    diamond = await dbfunc.fetchValue('diamond', 'misc', userid)
    gold_ingot = await dbfunc.fetchValue('gold_ingot', 'misc', userid)
    netherite_scrap = await dbfunc.fetchValue('netherite_scrap', 'misc', userid)
    netherite_ingot = await dbfunc.fetchValue('netherite_ingot', 'misc', userid)
    redstone = await dbfunc.fetchValue('redstone', 'misc', userid)
    soul_sand = await dbfunc.fetchValue('soul_sand', 'misc', userid)
    wood = await dbfunc.fetchValue('wood', 'misc', userid)
    bed = await dbfunc.fetchValue('bed', 'misc', userid)
    common_chest = await dbfunc.fetchValue('common_chest', 'misc', userid)
    rare_chest = await dbfunc.fetchValue('rare_chest', 'misc', userid)
    super_rare_chest = await dbfunc.fetchValue('super_rare_chest', 'misc', userid)
    epic_chest = await dbfunc.fetchValue('epic_chest', 'misc', userid)
    mythic_chest = await dbfunc.fetchValue('mythic_chest', 'misc', userid)
    legendary_chest = await dbfunc.fetchValue('legendary_chest', 'misc', userid)
    
    misc = {
        'emerald': emerald,
        'cobble': cobble,
        'coal': coal,
        'iron_ingot': iron_ingot,
        'diamond': diamond,
        'gold_ingot': gold_ingot,
        'netherite_scrap': netherite_scrap,
        'netherite_ingot': netherite_ingot,
        'redstone': redstone,
        'soul_sand': soul_sand,
        'wood': wood,
        'bed': bed,
        'common_chest': common_chest,
        'rare_chest': rare_chest,
        'super_rare_chest':super_rare_chest,
        'epic_chest': epic_chest,
        'mythic_chest': mythic_chest,
        'legendary_chest': legendary_chest
    }
    
    return misc