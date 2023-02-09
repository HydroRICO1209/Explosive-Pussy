from discord.ext import commands
import discord

class Database:
    def __init__(self, bot):
        self.bot = bot

    async def fetchValue(self, item, tablename, id, idtype): 
        #item, tablename, id, idtype
        fetch_query = f'SELECT {item} FROM {tablename} WHERE {idtype} = $1'
        return (await self.bot.db.fetchval(fetch_query, int(id)))
    
    async def updateIntValue(self, item, tablename, id, number, idtype):
        #item, tablename, id, number, idtype
        fetch_query = f'SELECT {item} FROM {tablename} WHERE {idtype} = $1'
        value = await self.bot.db.fetchval(fetch_query, int(id))
        newvalue = int(number) + value
        
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE {idtype} = $2'
        await self.bot.db.execute(update_query, int(newvalue), int(id))
        
    async def setStrValue(self, item, tablename, id, newStr, idtype):
        #item, tablename, id, newStr, idtype
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE {idtype} = $2'
        await self.bot.db.execute(update_query, newStr, int(id))
        
    async def setIntValue(self, item, tablename, id, number, idtype):
        #item, tablename, id, number, idtype
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE {idtype} = $2'
        await self.bot.db.execute(update_query, int(number), int(id))
    
    async def setBoolValue(self, item, tablename, id, value, idtype):
        #item, tablename, id, number, idtype
        update_query = f'UPDATE {tablename} SET {item} = $1 WHERE {idtype} = $2'
        await self.bot.db.execute(update_query, bool(value), int(id))