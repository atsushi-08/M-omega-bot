import discord
from discord.ext import commands
from core.classes import cog_extension
import json

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class React(cog_extension):
    @commands.command()
    async def 跪(self,ctx):
        pic = discord.File(jdata['dalao_pic'])
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))