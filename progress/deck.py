async def Deck(ctx):
    dbfunc = ctx.bot.database_handler

    userid = ctx.author.id
    cid = ctx.channel.id
    
    card1 = await dbfunc.fetchValue('card1', 'deck', cid, 'matchid')
    card2 = await dbfunc.fetchValue('card2', 'deck', cid, 'matchid')
    card3 = await dbfunc.fetchValue('card3', 'deck', cid, 'matchid')
    card4 = await dbfunc.fetchValue('card4', 'deck', cid, 'matchid')
    card5 = await dbfunc.fetchValue('card5', 'deck', cid, 'matchid')
    card6 = await dbfunc.fetchValue('card6', 'deck', cid, 'matchid')
    card7 = await dbfunc.fetchValue('card7', 'deck', cid, 'matchid')
    card8 = await dbfunc.fetchValue('card8', 'deck', cid, 'matchid')
    
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