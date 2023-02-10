async def Playercard(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    
    card1 = await dbfunc.fetchValue('card1', 'playercard', userid, 'playerid')
    card2 = await dbfunc.fetchValue('card2', 'playercard', userid, 'playerid')
    card3 = await dbfunc.fetchValue('card3', 'playercard', userid, 'playerid')
    card4 = await dbfunc.fetchValue('card4', 'playercard', userid, 'playerid')
    card5 = await dbfunc.fetchValue('card5', 'playercard', userid, 'playerid')
    card6 = await dbfunc.fetchValue('card6', 'playercard', userid, 'playerid')
    card7 = await dbfunc.fetchValue('card7', 'playercard', userid, 'playerid')
    card8 = await dbfunc.fetchValue('card8', 'playercard', userid, 'playerid')
    card9 = await dbfunc.fetchValue('card9', 'playercard', userid, 'playerid')
    card10 = await dbfunc.fetchValue('card10', 'playercard', userid, 'playerid')
    card11 = await dbfunc.fetchValue('card11', 'playercard', userid, 'playerid')
    card12 = await dbfunc.fetchValue('card12', 'playercard', userid, 'playerid')
    
    playercard = {
        'card1': card1,
        'card2': card2,
        'card3': card3,
        'card4': card4,
        'card5': card5,
        'card6': card6,
        'card7': card7,
        'card8': card8,
        'card9': card9,
        'card10': card10,
        'card11': card11,
        'card12': card12
    }
    
    return playercard