async def Deck(ctx):
    dbfunc = ctx.bot.database_handler
    cid = ctx.channel.id

    cardlist = await dbfunc.fetchValue('cardlist', 'deck', cid, 'matchid')
    
    deck = {
        'cardlist': cardlist
    }
    
    return deck