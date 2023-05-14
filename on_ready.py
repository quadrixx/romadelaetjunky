import discord
from discord.ext import commands

bot = discord.Bot()
@bot.event
async def on_ready():
    for server in bot.guilds:
        for channel in server.channels:
            if channel.name == 'основной':
                text_channel= channel.id
    await bot.get_channel(text_channel).send("bot is online")
bot.run('MTEwNzM5NTkxNjY2MDQ5MDI0MA.GsW_Wi.BGdsMPplqRRcG9etNGi0jE9vhlS0qBNdFyIFGM')
