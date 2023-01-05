import discord
from discord.ext import commands
import json
import asyncio
import random

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        await channel.send(f'新的臭ㄐㄐ{member}加入了!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        await channel.send(f'臭ㄐㄐ{member}離我們而去了...')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author == self.bot.user:
            return
        if msg.content == '我好帥喔':
            if msg.author.id == 560457069480640518:
                await msg.channel.send('沒錯蔡神最帥了')
            else:
                await msg.channel.send('並沒有，蔡神比較帥')
                await asyncio.sleep(1)
                tmp = await msg.channel.send('其實我比較帥')
                await asyncio.sleep(2)
                await tmp.delete()
        if msg.content == 'ㄞ' or msg.content == '跪':
            pic = discord.File(jdata['dalao_pic'])
            await msg.channel.send(file=pic)
        if msg.content == '這裡是哪裡':
            tmp = await msg.channel.send('這裡是男同俱樂部')
            await asyncio.sleep(2)
            await tmp.delete()
            await msg.channel.send('這裡是音遊人均學霸')
        if '月貓' in msg.content:
            await msg.channel.send('月貓生日快樂')
        if '郭' in msg.content or msg.author.id == 603522753303281667:
            if msg.content.startswith('!'):
                return
            list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
            a = random.choices(list)
            if a[0]<2:
                await msg.channel.send('謝謝郭神')
            else:
                pic = discord.File(jdata['kuo_img'])
                await msg.channel.send(file=pic)
        if '蔡' in msg.content or msg.author.id == 560457069480640518:
            if msg.content.startswith('!'):
                return
            await msg.channel.send('蔡神什麼時候女裝')
        if 'frums' in msg.content or 'Frums' in msg.content:
            await msg.channel.send('好難聽')

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Event(bot))