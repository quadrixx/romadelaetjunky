import discord
from discord.ext import commands


class url_listener(commands.Cog):
    def __init__(self, bot, list_of_urls):
        self.bot = bot
        self.lou = list_of_urls
        self.ready = False
    @commands.Cog.listener("on_message")
    async def listener(self, message):
        attachments = message.attachments
        if len(attachments) != 0:
            self.ready = True
            for att in attachments:
                self.lou.append(att.url)


