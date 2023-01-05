import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

gamewith = "https://shadowverse.gamewith.jp/article/show/84174"

class Shadowverse(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def sv(self,ctx,method):
        if method == "tier":
            response = requests.get(gamewith)
            soup = BeautifulSoup(response.text ,'html.parser')
            tier_list = soup.find_all("div",{"class":"sv_saikyo_table"})
            embed=discord.Embed(title="指定環境tier表", description="從gamewith抄來的，看看就好", color=0x2512b7)
            i = 1
            for tier in tier_list:
                tr = tier.find_all("tr")
                del tr[0]
                str = ""
                for item in tr:
                    a = item.find("a")
                    str = str + a.text + '\n'
                embed.add_field(name=f"tier {i}",value=str,inline=True)
                i = i + 1
            await ctx.send(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Shadowverse(bot))