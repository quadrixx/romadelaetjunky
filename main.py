import discord
from discord.ext import commands,bridge
from random import randint
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='j!', intents = intents)



@bot.slash_command()
async def roll(ctx):
    await ctx.respond(f'{ctx.user.name} загадал случайное число:{randint(0,100)}')
cogs_list = ['on_ready', 'all_listener','roll']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
bot.run('MTEwNzM5NTkxNjY2MDQ5MDI0MA.GsW_Wi.BGdsMPplqRRcG9etNGi0jE9vhlS0qBNdFyIFGM')