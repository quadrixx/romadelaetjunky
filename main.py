import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='j!', intents = intents)


list_of_messages = []
list_of_urls = []



cogs_list = ['on_ready', 'url_listener']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
bot.run('MTEwNzM5NTkxNjY2MDQ5MDI0MA.GsW_Wi.BGdsMPplqRRcG9etNGi0jE9vhlS0qBNdFyIFGM')