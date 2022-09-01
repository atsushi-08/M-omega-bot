import discord
from discord.ext import commands
import json

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Mybot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = '!',
            intents = discord.Intents.all(),
            application_id = jdata["app_id"])

    async def setup_hook(self):
        await self.load_extension("cmds.event")
        await self.load_extension("cmds.main")
        await self.load_extension("cmds.react")
        await self.load_extension("cmds.genshin")
        await self.load_extension("cmds.chunithm")

    async def on_ready(self):
        print("Ready!")

bot = Mybot()
bot.run(jdata["TOKEN"])