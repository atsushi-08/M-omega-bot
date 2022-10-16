import discord
from discord.ext import commands
import json
import os

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Mybot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = '!',
            intents = discord.Intents.all(),
            application_id = jdata["app_id"])

    async def setup_hook(self):
        for filename in os.listdir('./cmds'):
            if filename.endswith('.py'):
                await self.load_extension(f'cmds.{filename[:-3]}')
                print(f'{filename[:-3]} loaded')

    async def on_ready(self):
        print("Ready!")

bot = Mybot()

@bot.command()
async def reload(ctx):
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.reload_extension(f'cmds.{filename[:-3]}')
            print(f'{filename[:-3]} reloaded')
    await ctx.message.delete()

bot.run(jdata["TOKEN"])