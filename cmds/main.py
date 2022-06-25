from sqlite3 import Timestamp
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

with open('setting.json', 'r', encoding='utF8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(bot.latency*1000)} (ms)')

    @commands.command()
    async def hello(self, ctx):
        embed=discord.Embed(title="阿嬤", url="https://discord.com/oauth2/authorize?client_id=938781532913532958&permissions=0&scope=bot", description="阿嬤擔心你被欺負 所以跑這來了", color=0xffa200, 
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="Kalen", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        embed.set_thumbnail(url="https://cdnb.artstation.com/p/assets/images/images/019/585/027/large/yara-al-masry-pinku-2019.jpg?1564143260")
        embed.add_field(name="-hello", value="查看所有指令", inline=False)
        embed.add_field(name="-said \"字串\"", value="請阿嬤幫你傳話", inline=False)
        embed.add_field(name="-clean \"數量\"", value="阿嬤幫你把奇怪的話刪掉", inline=False)
        embed.add_field(name="-食物", value="阿嬤吃過的美食", inline=False)
        embed.add_field(name="-不堪回首", value="阿嬤都有把照片留下來", inline=False)
        embed.add_field(name="-色色", value="你喜歡甚麼阿嬤都知道", inline=False)
        embed.set_image(url="https://cdna.artstation.com/p/assets/images/images/040/000/112/large/yara-al-masry-kobaryo.jpg?1627559571")
        await ctx.send(embed=embed)

    @commands.command()
    async def said(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num : int):
        await ctx.channel.purge(limit = num+1)

def setup(bot):
    bot.add_cog(Main(bot))