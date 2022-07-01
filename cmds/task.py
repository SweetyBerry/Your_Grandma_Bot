import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime, random

class Task(Cog_Extension):

    #初始化
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        self.counter = 0

        #async def interval():  #重複任務
            #await self.bot.wait_until_ready()
            #self.channel = self.bot.get_channel(867733877580759063)
            #while not self.bot.is_closed():
                #await self.channel.send('Hi im running')
                #await asyncio.sleep(5)
    
        #self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():  #時間到任務
                await self.bot.wait_until_ready()
                self.channel = self.bot.get_channel(803996929327366166)
                while not self.bot.is_closed():
                    now_time = datetime.datetime.now().strftime('%H%M')
                    with open('setting.json', 'r', encoding='utF8') as jfile:
                        jdata = json.load(jfile)
                    if now_time == jdata['time'] and self.counter == 0:
                        await self.channel.send('有沒有人要陪我吃宵夜')
                        random_pic = random.choice(jdata['food_pic'])
                        await self.channel.send(random_pic)
                        self.counter = 1
                        await asyncio.sleep(1)
                    if now_time == '2301':
                        self.counter = 0
                        await asyncio.sleep(1)
                    else:
                        await asyncio.sleep(1)
                        pass    
                    
        
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command() #設定重複任務的Channel
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command() #設定時間(使用者傳入)
    async def set_time(self, ctx, time):
        with open('setting.json', 'r', encoding='utF8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', 'w', encoding='utF8') as jfile:
            json.dump(jdata, jfile, indent = 4)
        




def setup(bot):
    bot.add_cog(Task(bot))
