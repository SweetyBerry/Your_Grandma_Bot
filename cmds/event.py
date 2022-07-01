from ssl import CHANNEL_BINDING_TYPES
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random


with open('setting.json', 'r', encoding='utF8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        goodnight = ['晚安', '睡', '睡了']
        if msg.content in goodnight and msg.author != self.bot.user:
            await msg.channel.send('死小子搞到現在才在睡')
        if msg.content.startswith('等'):
            await msg.channel.send('要等到民國幾年')
        if msg.content.startswith('有人'):
            await msg.channel.send('沒有')
        if msg.content.startswith('ㄟ'):
            await msg.channel.send('要找誰')
        if msg.content.startswith('幹麻'):
            await msg.channel.send('起來嗨!')
        if msg.content.endswith('好色'):
            random_pic = random.choice(jdata['elo_pic'])
            await msg.channel.send(random_pic)



def setup(bot):
    bot.add_cog(Event(bot))