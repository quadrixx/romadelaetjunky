import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='j!', intents=intents)


token = open('token', 'r').readline().strip()
cogs_list = ['roll', 'gif', 'handshaking']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


bot.run(token)