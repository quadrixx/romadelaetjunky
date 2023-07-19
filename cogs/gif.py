import discord
from discord import Interaction
import requests
from Demogif import demotivate_gif
from bs4 import BeautifulSoup as bs
from discord.ext import commands
from discord.ui import InputText, Modal
import multiprocessing as mp
import asyncio
import concurrent.futures
import subprocess

executor = concurrent.futures.ThreadPoolExecutor(max_workers=999)
key = None
loop = asyncio.get_event_loop()

# проверяет типа гифки
def check(content):
    if content.startswith('https://tenor'):
        return True
    elif content.startswith('https://media'):
        return False
    else:
        return None


async def do(ctx, upper_text, lower_text):
    demotivate_gif(upper_text, lower_text, 'gifka.gif')
    await ctx.send(file=discord.File('out.gif'))


def tenor_parser(link: str):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    free_link_downloader(soup.select('[itemprop="contentUrl"]')[0]['content'])


def free_link_downloader(link: str):
    r = requests.get(link)
    with open('gifka.gif', 'wb') as f:
        f.write(r.content)


class MyModal(Modal):
    def __init__(self):
        super().__init__(title="Демотиватор")
        self.lower_text = None
        self.upper_text = None
        self.add_item(InputText(label='Верхний текст'))
        self.add_item(InputText(label='Нижний текст'))

    async def callback(self, interaction: discord.Interaction):
        self.upper_text = self.children[0].value
        self.lower_text = self.children[1].value
        embed = discord.Embed(title='waiting for gif', color=discord.Color.green())
        await interaction.response.send_message(embed=embed)


class GifProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel = None

    @commands.slash_command(name='demotivate')
    async def demotivate(self, ctx):
        modal = MyModal()
        channel = ctx.channel
        await ctx.interaction.response.send_modal(modal)
        while True:
            while True:
                msg = await self.bot.wait_for('message', timeout=30)

                if msg.author == ctx.author:
                    break
                else:
                    pass
            cnt = msg.content
            if check(cnt):
                tenor_parser(cnt)
                break
            elif not check(cnt):
                free_link_downloader(cnt)
                break
            else:
                pass
        demotivate_gif(modal.upper_text, modal.lower_text, 'gifka.gif')
        await ctx.send(file=discord.File('out.gif'))


def setup(bot):
    bot.add_cog(GifProcessor(bot))
