import random
from progress.deck import * 
from progress.itemlist import card_list

async def shufflestart(ctx):
    dbfunc = ctx.bot.database_handler
    userid = ctx.author.id
    cid = ctx.channel.id
    
    
    for card in card_list:
        is_done = False
        while is_done == False:
            deck = await Deck(ctx)
            randnum = random.randint(1,8)
            if deck[f'card{randnum}'] == 'rip bozo':
                item = f'card{randnum}'
                await dbfunc.setStrValue(item, 'deck', cid, card, 'matchid')
                is_done = True
            else:
                is_done = False