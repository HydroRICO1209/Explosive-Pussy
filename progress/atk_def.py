async def atk_def(ctx):
    dbfunc = self.bot.database_handler
    userid = ctx.author.id

    helmet = await dbfunc.fetchValue('helmet', 'armors', self.userid)
    chestplate = await dbfunc.fetchValue('chestplate', 'armors', self.userid)
    leggings = await dbfunc.fetchValue('leggings', 'armors', self.userid)
    boots = await dbfunc.fetchValue('boots', 'armors', self.userid)
    sword = await dbfunc.fetchValue('sword', 'armors', self.userid)
    level = await dbfunc.fetchValue('level', 'armors', self.userid)
    
    userdef = level * 1 
    if helmet == 0:
        userdef += 0
    elif helmet == 1:
        userdef += 3
    elif helmet == 2:
        userdef += 10
    elif helmet == 3:
        userdef += 20
    elif helmet == 4:
        userdef += 30
    elif helmet == 5:
        userdef += 40
    elif helmet == 6:
        userdef += 60
    elif helmet == 7:
        userdef += 70
    
    if chestplate == 0:
        userdef += 0
    elif chestplate == 1:
        userdef += 12
    elif chestplate == 2:
        userdef += 25
    elif chestplate == 3:
        userdef += 60
    elif chestplate == 4:
        userdef += 70
    elif chestplate == 5:
        userdef += 100
    elif chestplate == 6:
        userdef += 130
    elif chestplate == 7:
        userdef += 200

    if leggings == 0:
        userdef += 0
    elif leggings == 1:
        userdef += 7
    elif leggings == 2:
        userdef += 20
    elif leggings == 3:
        userdef += 35
    elif leggings == 4:
        userdef += 40
    elif leggings == 5:
        userdef += 50
    elif leggings == 6:
        userdef += 65
    elif leggings == 7:
        userdef += 80

    if boots == 0:
        userdef += 0
    elif boots == 1:
        userdef += 3
    elif boots == 2:
        userdef += 8
    elif boots == 3:
        userdef += 15
    elif boots == 4:
        userdef += 20
    elif boots == 5:
        userdef += 30
    elif boots == 6:
        userdef += 45
    elif boots == 7:
        userdef += 50

    useratk = level * 1
    if sword == 0:
        useratk += 0
    elif sword == 1:
        useratk += 20
    elif sword == 2:
        useratk += 70
    elif sword == 3:
        useratk += 95  
    elif sword == 4:
        useratk += 130
    elif sword == 5:
        useratk += 190
    elif sword == 6:
        useratk += 275
    elif sword == 7:
        useratk += 400
    elif sword == 69:
        useratk += 30

    await dbfunc.setIntValue('atk', 'stats', userid, useratk)
    await dbfunc.setIntValue('defend', 'stats', userid, userdef)