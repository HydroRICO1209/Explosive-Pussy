async def Deck(ctx):
    dbfunc = ctx.bot.database_handler
    cid = ctx.channel.id
    
    card1 = await dbfunc.fetchValue('card1', 'deck', cid, 'matchid')
    card2 = await dbfunc.fetchValue('card2', 'deck', cid, 'matchid')
    card3 = await dbfunc.fetchValue('card3', 'deck', cid, 'matchid')
    card4 = await dbfunc.fetchValue('card4', 'deck', cid, 'matchid')
    card5 = await dbfunc.fetchValue('card5', 'deck', cid, 'matchid')
    card6 = await dbfunc.fetchValue('card6', 'deck', cid, 'matchid')
    card7 = await dbfunc.fetchValue('card7', 'deck', cid, 'matchid')
    card8 = await dbfunc.fetchValue('card8', 'deck', cid, 'matchid')
    card9 = await dbfunc.fetchValue('card9', 'deck', cid, 'matchid')
    card10 = await dbfunc.fetchValue('card10', 'deck', cid, 'matchid')
    card11 = await dbfunc.fetchValue('card11', 'deck', cid, 'matchid')
    card12 = await dbfunc.fetchValue('card12', 'deck', cid, 'matchid')
    
    deck = {
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
    
    return deck