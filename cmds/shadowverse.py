import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from discord.ui import Select,View,Button

gamewith = "https://shadowverse.gamewith.jp/article/show/84174"
response = requests.get(gamewith)
soup = BeautifulSoup(response.text ,'html.parser')
tier_list = soup.find_all("div",{"class":"sv_saikyo_table"})

def check_career(str):
    if 'エルフ' in str:
        return "精靈"
    if 'ロイヤル' in str:
        return "皇家"
    if 'ウィッチ' in str:
        return "巫師"
    if 'ドラゴン' in str:
        return "龍族"
    if 'ネクロ' in str:
        return "死靈"
    if 'ヴァンプ' in str:
        return "吸血鬼"
    if 'ビショップ' in str:
        return "主教"
    if 'ネメシス' in str:
        return "復仇者"

career = {}
url = {}
for tier in tier_list:
    tr = tier.find_all("tr")
    del tr[0]
    for item in tr:
        a = item.find("a")
        deck_name = a.text
        career[deck_name] = check_career(deck_name)
        url[deck_name] = a["href"]

class Shadowverse(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def sv(self,ctx,method):
        if method == "tier":
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
        if method == "deck":
            select_career = Select(
                placeholder="選擇職業",
                options=[discord.SelectOption(
                    label='精靈'
                ),discord.SelectOption(
                    label='皇家'
                ),discord.SelectOption(
                    label='巫師'
                ),discord.SelectOption(
                    label='龍族'
                ),discord.SelectOption(
                    label='死靈'
                ),discord.SelectOption(
                    label='吸血鬼'
                ),discord.SelectOption(
                    label='主教'
                ),discord.SelectOption(
                    label='復仇者'
                ),]
            )

            async def select_career_callback(interaction):
                chosen_career = select_career.values[0]
                select_deck = Select(
                    placeholder="選擇牌組",
                    options=[]
                )
                for item in career:
                    if career[item] == chosen_career:
                        select_deck.append_option(discord.SelectOption(
                            label=item,
                            value=url[item]
                        ))

                async def select_deck_callback(interaction):
                    await interaction.response.send_message(select_deck.values[0])
                    
                select_deck.callback = select_deck_callback
                deck_view = View()
                deck_view.add_item(select_deck)
                await interaction.response.send_message(view = deck_view)

            select_career.callback = select_career_callback
            view = View()
            view.add_item(select_career)
            await ctx.send(view=view)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Shadowverse(bot))