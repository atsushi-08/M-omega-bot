from encodings import utf_8
import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents = intents)

@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    print(f'{extension} loaded')
    await ctx.message.delete()

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    print(f'{extension} reloaded')
    await ctx.message.delete()

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    print(f'{extension} unloaded')
    await ctx.message.delete()

for filename in os.listdir('./cmds'):
    if(filename.endswith('.py')):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
