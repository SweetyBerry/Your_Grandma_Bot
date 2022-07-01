import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utF8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):

    @commands.command()
    async def 食物(self, ctx):
        random_pic = random.choice(jdata['food_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def 不堪回首(self, ctx):
        random_pic = random.choice(jdata['past_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def 色色(self, ctx):
        random_pic = random.choice(jdata['anime_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def 笑話(self, ctx):
        random_pic = random.choice(jdata['laugh'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))