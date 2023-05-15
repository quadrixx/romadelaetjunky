import discord
from discord.ext import commands
from on_ready import OnReadyCog, setup
from Demotivor import Demotivator
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='j!', intents = intents)


list_of_messages = []
list_of_urls = []

@bot.event
async def on_message(message):
    print(message.content)




setup(bot)

bot.run('MTEwNzM5NTkxNjY2MDQ5MDI0MA.GsW_Wi.BGdsMPplqRRcG9etNGi0jE9vhlS0qBNdFyIFGM')