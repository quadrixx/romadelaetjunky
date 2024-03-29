import discord
from discord.ext import commands
import atexit
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='j!', intents=intents)


token = open('token', 'r').readline().strip()
cogs_list = ['roll', 'gif', 'handshaking', 'all_listener']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)


atexit.register(bot.cogs['MsgListener'].end)
