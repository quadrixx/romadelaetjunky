from discord.ext import commands
import discord
from Demotivor import demotivate
import random
import asyncio
from emoji import replace_emoji
import os


# функция, которая проверяет содержание сообщения
def msg_filter(msg):
    if msg[0:5] == "https" or len(msg) > 60 or msg.startswith('j!'):
        return False
    else:
        return True


# функция, которая очищает сообщения от смайликов
def dispose_of_emojis(string):
    result = replace_emoji(string, replace='')
    while '<' in result and '>' in result:
        result = result.replace(result[result.index('<'):result.index('>') + 1], '')
    return result


class MsgListener(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.channel = None

    # когда бот врубается, проверяет наличие отдельный папки для каждого сервера, на которых он пашет
    @commands.Cog.listener()
    async def on_ready(self):
        folders = os.listdir('servers')
        for guild in self.bot.guilds:
            name = guild.name
            if name not in folders:
                os.mkdir(f'servers//{name}')
                for i in ['msgs', 'urls']:
                    with open(f'servers//{name}//{i}.txt', 'w') as f:
                        f.write('')
        print('all is done')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        name = guild.name
        os.mkdir(f'servers//{name}')
        for i in ['msgs', 'urls']:
            with open(f'servers//{name}//{i}.txt', 'w') as f:
                f.write('')

    # listener in charge of managing msgs
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        guild = message.channel.guild
        f = open(f'servers//{guild}//channel.txt', 'r')
        chn = f.readline()
        f.close()
        if message.channel.name == chn:
            cnt = message.content
            if msg_filter(cnt):
                cnt = dispose_of_emojis(cnt)
                with open(f'servers//{guild}//msgs.txt', 'a') as f:
                    f.write(f'\n{cnt}')



    @commands.command()
    async def set(self, ctx):
        channels = ctx.guild.channels
        for i in channels:
            name = i.name
            if ctx.message.content[6::] == name:
                self.channel = discord.utils.get(channels, name=name)
                with open(f'servers//{ctx.guild}//channel.txt', 'w') as f:
                    f.write(name)
                await ctx.send(embed=discord.Embed(title=f'junky is running on "{name}"', colour=discord.Color.green()))
                break
        else:
            await ctx.send(embed=discord.Embed(title='channel not found', colour=discord.Color.red()))


class Counter:
    def __init__(self, lom: list, lou: list, len_restriction: int) -> None:
        self.lom = lom
        self.lou = lou
        self.len_restriction = len_restriction

    def check_for_msgs(self, lom):
        return len(lom) <= self.len_restriction


def setup(bot):
    bot.add_cog(MsgListener(bot))
