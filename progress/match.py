async def Match(ctx):
    dbfunc = ctx.bot.database_handler

    cid = ctx.channel.id
    
    matchhostid = await dbfunc.fetchValue('matchhostid', 'match', cid, 'matchid')
    matchstarted = await dbfunc.fetchValue('matchstarted', 'match', cid, 'matchid')
    matchtotalplayer = await dbfunc.fetchValue('matchtotalplayer', 'match', cid, 'matchid')
    
    match = {
        'matchhostid': matchhostid,
        'matchstarted': matchstarted,
        'matchtotalplayer': matchtotalplayer,
    }
    
    return match