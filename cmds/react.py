import discord
from discord.ext import commands
import json
from discord.ui import Button,View,Select

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class React(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def button_test(self,ctx):
        view = View()
        button = Button(label='點我啊臭ㄐㄐ',style=discord.ButtonStyle.primary,emoji='<:ji:816467849357951058>')

        async def button_callback(interaction):
            user = interaction.user.name
            await interaction.response.send_message(f'{user}點了，{user}是臭ㄐㄐ')
        button.callback = button_callback
        view.add_item(button)
        await ctx.send(view=view)

    @commands.command()
    async def select_test(self,ctx):
        select = Select(
            placeholder='你覺得蔡神有多帥(滿分100)',
            options=[
                discord.SelectOption(
                    label='100分',
                    description='滿分，蔡神超帥'
                ),
                discord.SelectOption(
                    label='200分',
                    description='蔡神怎麼可能被100分侷限住'
                ),
                discord.SelectOption(
                    label='114514分',
                    description='這麼臭的選項有存在的必要嗎(惱'
                )
            ]
        )
        async def callback(interaction):
            user = interaction.user.name
            await interaction.response.send_message(f'{user}覺得蔡神有{select.values[0]}帥')

        select.callback = callback
        view = View()
        view.add_item(select)
        await ctx.send(view = view)

async def setup(bot):
    await bot.add_cog(React(bot))