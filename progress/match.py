async def Match(ctx):
    dbfunc = bot.database_handler

    cid = ctx.channel.id
    
    player1id = await dbfunc.fetchValue('player1id', 'match', cid, 'matchid')
    player2id = await dbfunc.fetchValue('player2id', 'match', cid, 'matchid')
    player3id = await dbfunc.fetchValue('player3id', 'match', cid, 'matchid')
    player4id  = await dbfunc.fetchValue('player4id', 'match', cid, 'matchid')
    
    match = {
        'player1id': player1id,
        'player2id': player2id,
        'player3id': player3id,
        'player4id': player4id
    }
    
    return match