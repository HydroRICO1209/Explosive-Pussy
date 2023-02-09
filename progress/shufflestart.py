import random
from progress.deck import * 
from progress.itemlist import card_list

async def shufflestart(ctx):
    dbfunc = self.bot.database_handler
    userid = ctx.author.id
    cid = ctx.channel.id
    is_done = False
    
    for card in card_list:
        while is_done == False:
            randnum = random.randint(1,8)
            if deck[f'card{randnum}'] == 'rip bozo':
                item = f'card{1}'
                await dbfunc.setStrValue(card, 'deck', cid, card_list[randnum], 'matchid')
                is_done = True
            else:
                is_done = False