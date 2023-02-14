async def Playercard(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    
    playercard_list = await dbfunc.fetchValue('playercard_list', 'playercard', userid, 'playerid')
    
    playercard = {
        'playercard_list': playercard_list
    }
    
    return playercard