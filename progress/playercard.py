async def Playercard(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    
    player_cardlist = await dbfunc.fetchValue('player_cardlist', 'playercard', userid, 'playerid')
    
    playercard = {
        'player_cardlist': player_cardlist
    }
    
    return playercard