import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents = intents)

@bot.event
async def on_ready():
    print("Ready!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(767679195698429965)
    await channel.send(f'新的臭ㄐㄐ{member}加入了!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(767679195698429965)
    await channel.send(f'臭ㄐㄐ{member}離我們而去了...')

bot.run('OTk1ODc3MjgzNjE5NDE0MDY2.Gep9pL.p6RMheEFP63XrbCRDMS6TvErNs78s754PlHOo0')
