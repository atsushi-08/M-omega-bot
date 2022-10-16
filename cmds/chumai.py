from openpyxl import load_workbook
import discord
from discord.ext import commands

class Chumai(commands.Cog):
    def __init__(self,bot :commands.Bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def 中二(self,ctx,name,dif,*score):
        def rating(base,sc):
            if sc>1009000:
                return round(base+2.15,2)
            elif sc>1007500:
                return round(base+2+(sc-1007500)/10000,3)
            elif sc>1005000:
                return round(base+1.5+(sc-1005000)/5000,3)
            elif sc>1000000:
                return round(base+1+(sc-1000000)/10000,3)
            else:
                return round(base+(sc-975000)/25000,3)

        wb = load_workbook('中二定數.xlsx')
        find = 0
        for sheet in wb:
            if find == 1:
                break
            for row in sheet.iter_rows(min_col=1,max_col=4):
                if row[0].value == name and row[1].value == dif:
                    find = 1
                    await ctx.send(f'{name} {dif}的定數是{row[3].value}')
                    if len(score)!=0:
                        await ctx.send(f'打{score[0]}分的R值是{rating(row[3].value,int(score[0]))}')

        if find == 0:
            await ctx.send('找不到這首歌')

    @commands.command()
    async def mai(self,ctx,name,dif,*other):
        type = None
        score = None

        def is_num(str):
            try:
                float(str)
                return True
            except ValueError:
                pass
            return False

        if len(other)!=0:
            for item in other:
                if is_num(item):
                    score = float(item)
                else:
                    type = item


        wb = load_workbook("mai定數.xlsx")
        list = []
        for sheet in wb:
            for row in sheet.iter_rows(min_col=1,max_col=5):
                if row[0].value == name and row[3].value == dif:
                    values = [cell.value for cell in row]
                    list.append(values)

        if len(list) == 2 and type == None:
            await ctx.send("這首歌有兩個譜面，你是要STD譜還是DX譜")

            def check(m):
                return (m.content == "DX" or m.content == "STD") and m.channel == ctx.channel
            msg = await self.bot.wait_for("message",check=check)
            type = msg.content
            for item in list:
                if item[2] == type:
                    await ctx.send(f'{name} {dif}({type}譜)的定數是{item[4]}')
        elif len(list) == 2 and type != None:
            for item in list:
                if item[2] == type:
                    await ctx.send(f'{name} {dif}({type}譜)的定數是{item[4]}')
        elif len(list) == 1:
            item = list[0]
            await ctx.send(f'{name} {dif}的定數是{item[4]}')
        else:
            await ctx.send('找不到這首歌')

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Chumai(bot))