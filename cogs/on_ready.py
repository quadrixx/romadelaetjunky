import discord
from discord.ext import commands


class OnReadyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print('1')
        """test_channel = 'null'
        for server in self.bot.guilds:
            for channel in server.channels:
                if channel.name == "тестовый":
                    test_channel = channel.id
        if test_channel != 'null':
            await self.bot.get_channel(test_channel).send("bot is online")"""


def setup(bot):
    bot.add_cog(OnReadyCog(bot))