import asyncio
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
        await self.load_extension(f"cmds.event")
        await self.load_extension(f"cmds.main")
        await self.load_extension(f"cmds.react")
        await self.load_extension(f"cmds.genshin")

    async def on_ready(self):
        print("Ready!")

bot = Mybot()
bot.run(jdata["TOKEN"])