async def Playerlist(ctx):
    dbfunc = ctx.bot.database_handler
    cid = ctx.channel.id
    
    player_list = await dbfunc.fetchValue('userid', 'playerlist', cid, 'matchid')
    
    playerlist = {
        'player_list': player_list
    }
    
    return playerlist