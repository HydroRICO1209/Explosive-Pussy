import random
from progress.deck import * 
from progress.itemlist import card_list

async def shufflestart(ctx):
    dbfunc = ctx.bot.database_handler
    userid = ctx.author.id
    cid = ctx.channel.id
    
    deck = await Deck(ctx)
    card = random.shuffle(deck['cardlist'])
    await dbfunc.setStrValue('deck', 'deck', cid, card, 'matchid')