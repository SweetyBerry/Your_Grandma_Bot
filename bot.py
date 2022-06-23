import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print("<< Bot is online >>")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(989142045325156372)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(989142045325156372)
    await channel.send(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')

bot.run("OTM4NzgxNTMyOTEzNTMyOTU4.GJGSu2.OiIflqq_8ACcgWiI_WY7rEh_ROkoFUUmocgWb8")
