from discord.ext import commands
import discord

class Database:
    def __init__(self, bot):
        self.bot = bot

    async def fetchValue(self, item, tablename, userid): 
        #item, tablename, userid
        fetch_query = f'SELECT {item} FROM {tablename} WHERE playerid = $1'
        return (await self.bot.db.fetchval(fetch_query, int(userid)))
    
    async def updateIntValue(self, item, tablename, userid, number):
        #item, tablename, userid, number
        fetch_query = f'SELECT {item} FROM {tablename} WHERE playerid = $1'
        value = await self.bot.db.fetchval(fetch_query, int(userid))
        newvalue = int(number) + value
        
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE playerid = $2'
        await self.bot.db.execute(update_query, int(newvalue), int(userid))
        
    async def setIntValue(self, item, tablename, userid, number):
        #item, tablename, userid, number
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE playerid = $2'
        await self.bot.db.execute(update_query, int(number), int(userid))
        
    async def updateStrValue(self, item, tablename, userid, newStr):
        #item, tablename, userid, newStr
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE playerid = $2'
        await self.bot.db.execute(update_query, newStr, int(userid))