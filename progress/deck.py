async def Deck(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    matchid = ctx.channel.id
    
    card1 = await dbfunc.fetchValue('card1', 'deck', matchid, 'matchid')
    card2 = await dbfunc.fetchValue('card2', 'deck', matchid, 'matchid')
    card3 = await dbfunc.fetchValue('card3', 'deck', matchid, 'matchid')
    card4 = await dbfunc.fetchValue('card4', 'deck', matchid, 'matchid')
    card5 = await dbfunc.fetchValue('card5', 'deck', matchid, 'matchid')
    card6 = await dbfunc.fetchValue('card6', 'deck', matchid, 'matchid')
    card7 = await dbfunc.fetchValue('card7', 'deck', matchid, 'matchid')
    card8 = await dbfunc.fetchValue('card8', 'deck', matchid, 'matchid')
    
    deck = {
        'card1': card1,
        'card2': card2,
        'card3': card3,
        'card4': card4,
        'card5': card5,
        'card6': card6,
        'card7': card7,
        'card8': card8
    }
    
    return deck