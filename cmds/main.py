from datetime import datetime
import discord
from discord.ext import commands
import random

numbers = ("1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟")

class Main(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def poll(self,ctx,question,*options):
        embed = discord.Embed(
            title = question,
            description = "投票啦臭ㄐㄐ",
            color = ctx.author.color
        )
        fields = [("選項","\n".join([f'{numbers[i]}: {option}' for i,option in enumerate(options)]),False)]

        for name,value,inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        
        await ctx.message.delete()
        message = await ctx.send(embed=embed)
        for emoji in numbers[:len(options)]:
            await message.add_reaction(emoji)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def 蔡神字串(self,ctx,new:str):
        msgid = 999926319481622598
        channel = self.bot.get_channel(767679195698429965)
        msg = await ctx.fetch_message(msgid)
        await msg.edit(content = msg.content + new)
        await ctx.message.delete()
        now = datetime.now()
        await channel.send(f'{now} 蔡神字串新增: {new}')
        await channel.send(f'現在蔡神字串有{len(msg.content+new)}字')

    @commands.command()
    async def 黃神字串(self,ctx,new:str):
        msgid = 1006532798548553818
        channel = self.bot.get_channel(767679195698429965)
        msg = await ctx.fetch_message(msgid)
        await msg.edit(content = msg.content + new)
        await ctx.message.delete()
        now = datetime.now()
        await channel.send(f'{now} 黃神字串新增: {new}')
        await channel.send(f'現在黃神字串有{len(msg.content+new)}字')

    @commands.command()
    async def 蔡神歐洲(self,ctx,new:str):
        msgid = 1025759331993530469
        channel = self.bot.get_channel(767679195698429965)
        msg = await ctx.fetch_message(msgid)
        await msg.edit(content = msg.content + '\n' + new)
        await ctx.message.delete()
        await channel.send(f"蔡神的歐洲事蹟又增加啦！\n祂{new}\n謝謝蔡團長海放")
        
    @commands.command()
    async def 隨機數(self,ctx,low:float,high:float):
        num = round(random.uniform(low*10,high*10))/10
        await ctx.send(f'抽到{round(num,1)}')

    @commands.command()
    async def test(self,ctx):
        embed = discord.Embed(title="測試")
        embed.set_image(url="https://img.gamewith.jp/article_tools/shadowverse/gacha/381276_i.png")
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Main(bot))