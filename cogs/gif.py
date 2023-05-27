import discord
import requests
import json
from bs4 import BeautifulSoup as bs
from discord.ext import commands


key = 'AIzaSyAaxn_f4rZAW89i65kxc4jNxFDx414_gtU'

#проверяет типа гифки
def check(content):
    if content.startswith('https://tenor'):
        return True
    elif content.startswith('https://media'):
        return False
    else:
        return None


def tenor_parser(link: str):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    free_link_downloader(soup.select('[itemprop="contentUrl"]')[0]['content'])


def free_link_downloader(link: str):
    r = requests.get(link)
    with open('gifka.gif', 'wb') as f:
        f.write(r.content)


class GifProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def demotivate(self, ctx):
        while True:
            msg = await self.bot.wait_for('message')
            cnt = msg.content
            if check(cnt):
                tenor_parser(cnt)
                a = await ctx.send(file = discord.File('gifka.gif'))
                print(a.attachments)
                break
            elif not check(cnt):
                free_link_downloader(cnt)
                a = await ctx.send(file=discord.File('gifka.gif'))
                break
            else:
                ctx.send("это не гифка")


def setup(bot):
    bot.add_cog(GifProcessor(bot))
