import pickle
import multiprocessing
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


def add(listener, message):
    name = message.guild.name
    cnt = dispose_of_emojis(message.content)
    if msg_filter(cnt):
        listener.lstner[name].append(cnt)
    listener.callback(name)


def do_demotivator(msgs: list):
    a, b = msgs[random.randint(0, len(msgs))], msgs[random.randint(0, len(msgs))]


class MsgListener(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.pool = multiprocessing.Pool()
        self.lstner = {}
        self.bot = bot
        self.len_restriction = 10
        self.channel = None

    # когда бот врубается, проверяет наличие отдельный папки для каждого сервера, на которых он пашет
    @commands.Cog.listener()
    async def on_ready(self):
        with open('save.pkl', 'rb') as f:
            self.lstner = pickle.load(f)
        for guild in self.bot.guilds:
            self.lstner.setdefault(guild.name, [])

    @commands.Cog.listener()
    async def on_disconnect(self):
        with open('save.pkl', 'wb') as d:
            pickle.dump(self.lstner, d)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.lstner.update(dict([guild.name, []]))

    @commands.Cog.listener()
    async def on_message(self, msg):
        if self.channel:
            self.pool.apply(add, (msg,))
        else:
            await msg.channel.send("channel is NOT set")
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
    def callback(self, name):
        if len(self.lstner[name]) == self.len_restriction:


class Guild:
    def __init__(self, len_restricton, lof, lou, channel):
        self.len_restriction = len_restricton
        self.lof = lof
        self.lou = lou


def setup(bot):
    bot.add_cog(MsgListener(bot))
