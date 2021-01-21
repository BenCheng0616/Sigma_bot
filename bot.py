import discord
from discord.ext import commands
import json
import random

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = 's!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f'{member} leave..')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def pic(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)

bot.run(jdata['TOKEN'])
