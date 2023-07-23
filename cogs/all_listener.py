import pickle
import multiprocessing
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


def do_demotivator(msgs: list):
    a, b = msgs[random.randint(0, len(msgs))], msgs[random.randint(0, len(msgs))]


class MsgListener(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.lstner = {'emptiness': Guild('emptiness', 50, [], []), 'клуб хейтеров': Guild('клуб хейтеров', 50, [], [])}
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
        self.lstner.update(dict([guild.name, Guild(guild.name, 50)]))

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel == self.lstner[msg.guild.name].channel:
            if len(msg.attachments) != 0:
                self.lstner[msg.guild.name].lou.append(msg.attachments[0].url)
            cnt = dispose_of_emojis(msg.content)
            if msg_filter(cnt) and cnt != '':
                self.lstner[msg.guild.name].lom.append(cnt)

    @commands.command()
    async def set(self, ctx):
        self.lstner[ctx.guild.name].channel = ctx.channel

    @commands.command()
    async def check(self, ctx):
        for i,j in self.lstner.items():
            print(f'{i}:{j.lom}')
    @commands.command()
    async def c(self,ctx):
        print(self.lstner['emptiness'].channel == self.lstner['клуб хейтеров'].channel)
        print(self.lstner['emptiness'].channel is self.lstner['клуб хейтеров'].channel)


class Guild:
    def __init__(self, name, len_restricton, lom, lou, channel=None):
        self.name = name
        self.len_restriction = len_restricton
        self.pic_restriction = 20
        self.lom = lom
        self.lou = lou
        self.channel = channel

    def callback(self):
        if len(self.lom) >= self.len_restriction and len(self.lou) >= self.pic_restriction:
            print('demoready')



def setup(bot):
    bot.add_cog(MsgListener(bot))
