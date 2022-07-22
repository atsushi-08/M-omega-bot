import discord
from discord.ext import commands
from core.classes import cog_extension
import json
import asyncio

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(cog_extension):
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
                tmp = await msg.channel.send('其實我比較帥')
                await asyncio.sleep(2.5)
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

def setup(bot):
    bot.add_cog(Event(bot))