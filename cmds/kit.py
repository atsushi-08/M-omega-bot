import discord
from discord.ext import commands
import random
from openpyxl import load_workbook

class Kit(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def 抽歌(self,ctx,game,lower,*upper):
        if len(upper)==0:
            upper = [float(lower)]

        if game == '中二':
            wb = load_workbook('中二定數.xlsx')
            list = []
            for sheet in wb:
                for row in sheet.iter_rows(min_col=1,max_col=4):
                    if row[3].value >= float(lower) and row[3].value <= float(upper[0]):
                        list.append([row[0].value,row[1].value])

        if game == 'mai':
            wb = load_workbook('mai定數.xlsx')
            list = []
            for sheet in wb:
                for row in sheet.iter_rows(min_col=1,max_col=5):
                    if row[4].value >= float(lower) and row[4].value <= float(upper[0]):
                        list.append([f'{row[0].value} ({row[2].value}譜)',row[3].value])

        if len(list) == 0:
            await ctx.send('無符合條件的歌')
        else:
            song = random.choice(list)
            await ctx.send(f"{song[0]} {song[1]}")
        

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Kit(bot))