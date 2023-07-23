import pickle
import multiprocessing

import requests
from discord.ext import commands
import discord
from Demotivor import demotivate
import random
import asyncio
from emoji import replace_emoji
import os
import threading


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


def do_demotivator(msgs: list, urls: list, name, channel, loop):
    upper, lower = msgs[random.randint(0, len(msgs) - 1)], msgs[random.randint(0, len(msgs) - 1)]
    pic = urls[random.randint(0, len(urls) - 1)]

    demotivate(upper, lower, pic, name)
    loop.create_task(channel.send(file=discord.File(f'{name}.png')))


class MsgListener(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.lstner = {'emptiness': Guild('emptiness', 50, [], []), 'клуб хейтеров': Guild('клуб хейтеров', 10, [], [])}

    # когда бот врубается, проверяет наличие отдельный папки для каждого сервера, на которых он пашет
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.lstner)

    @commands.Cog.listener()
    async def on_disconnect(self):
        with open('save.pkl', 'wb') as d:
            pickle.dump(self.lstner, d)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.lstner.update(dict([guild.name, Guild(guild.name, 50, [], [])]))

    @commands.Cog.listener()
    async def on_message(self, msg):
        name = msg.guild.name
        if msg.channel == self.lstner[name].channel:
            if len(msg.attachments) != 0:
                self.lstner[name].lou.append(msg.attachments[0].url)
            cnt = dispose_of_emojis(msg.content)
            if msg_filter(cnt) and cnt != '':
                self.lstner[name].lom.append(cnt)
            self.lstner[name].callback(self.bot.loop)

    @commands.command()
    async def set(self, ctx):
        self.lstner[ctx.guild.name].channel = ctx.channel

    @commands.command()
    async def check(self, ctx):
        for i, j in self.lstner.items():
            print(f'{i}:{j.lom}')

    @commands.command()
    async def c(self, ctx):
        print(self.lstner['emptiness'].channel == self.lstner['клуб хейтеров'].channel)
        print(self.lstner['emptiness'].channel is self.lstner['клуб хейтеров'].channel)


class Guild:
    def __init__(self, name, len_restricton, lom, lou, channel=None):
        self.name = name
        self.len_restriction = len_restricton
        self.pic_restriction = 2
        self.lom = lom
        self.lou = lou
        self.channel = channel

    def callback(self, loop):
        print(self.lom, self.lou)
        if len(self.lom) >= self.len_restriction and len(self.lou) >= self.pic_restriction:
            print('qweqweaxdfzxcdfgghdfghrfgdfdd')
            thread = threading.Thread(target=do_demotivator, args=(self.lom, self.lou, self.name, self.channel, loop))
            thread.start()
            thread.join()
            self.lom = []
            self.lou = []


def setup(bot):
    bot.add_cog(MsgListener(bot))
