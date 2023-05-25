import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='j!', intents = intents)


cogs_list = ['all_listener','roll', 'gif']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


bot.run('MTEwNzM5NTkxNjY2MDQ5MDI0MA.GsW_Wi.BGdsMPplqRRcG9etNGi0jE9vhlS0qBNdFyIFGM')