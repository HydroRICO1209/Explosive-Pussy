async def Playerlist(ctx):
    dbfunc = bot.database_handler

    cid = ctx.channel.id
    
    player1id = await dbfunc.fetchValue('player1id', 'playerlist', cid, 'matchid')
    player2id = await dbfunc.fetchValue('player2id', 'playerlist', cid, 'matchid')
    player3id = await dbfunc.fetchValue('player3id', 'playerlist', cid, 'matchid')
    player4id  = await dbfunc.fetchValue('player4id', 'playerlist', cid, 'matchid')
    
    playerlist = {
        'player1id': player1id,
        'player2id': player2id,
        'player3id': player3id,
        'player4id': player4id
    }
    
    return playerlist