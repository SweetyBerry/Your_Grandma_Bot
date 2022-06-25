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
        Keyword = ['apple', 'tank', 'pie']
        if msg.content in Keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')
        if msg.content.endswith('好色'):
            random_pic = random.choice(jdata['elo_pic'])
            await msg.channel.send(random_pic)



def setup(bot):
    bot.add_cog(Event(bot))