import discord
from discord.ext import commands
from discord.ui import Select,View,Button
import sys
sys.path.append('../discordbot')
from discordbot import crawldeck

tournament_tier = crawldeck.load()
career = tournament_tier[0]
url = tournament_tier[1]
tier = tournament_tier[2]
deck_list = tournament_tier[3]

class Shadowverse(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def sv(self,ctx,method):
        if method == "tier":
            embed=discord.Embed(title="指定環境tier表", description="從gamewith抄來的，看看就好", color=0x2512b7)
            i = 1
            for list in tier:
                str = ""
                for item in list:
                    str = str + item +'\n'
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
        if method == "pro_deck":
            tmp = crawldeck.load_pro_deck()
            pro_deck = tmp[0]
            url = tmp[1]
            select_pro_deck = Select(
                    placeholder="選擇牌組",
                    options=[]
                )
            for item in pro_deck:
                select_pro_deck.append_option(discord.SelectOption(
                    label=f"{item[0]}{item[1]} {item[2]} {item[3]}",
                    )
                )
            
            
            pro_deck_view = View()
            pro_deck_view.add_item(select_pro_deck)
            await ctx.send(view=pro_deck_view)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Shadowverse(bot))