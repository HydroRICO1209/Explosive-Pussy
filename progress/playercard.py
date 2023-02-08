async def Playercard(self, ctx):
    dbfunc = bot.database_handler

    userid = ctx.author.id
    
    card1 = await dbfunc.fetchValue('card1', 'playercard', userid, 'playerid')
    card2 = await dbfunc.fetchValue('card2', 'playercard', userid, 'playerid')
    card3 = await dbfunc.fetchValue('card3', 'playercard', userid, 'playerid')
    
    playercard = {
        'card1': card1,
        'card2': card2,
        'card3': card3
    }
    
    return playercard