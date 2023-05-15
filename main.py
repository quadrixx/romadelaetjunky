import discord
from discord.ext import commands
from on_ready import OnReadyCog

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='j!', intents = intents)

bot.add_cog(OnReadyCog(bot))








bot.run('MTEwNzM5NTkxNjY2MDQ5MDI0MA.GsW_Wi.BGdsMPplqRRcG9etNGi0jE9vhlS0qBNdFyIFGM')