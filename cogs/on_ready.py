import discord
from discord.ext import commands


class OnReadyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('a'*60)


    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        await self.bot.fetch_channel('1107399217313501345')
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