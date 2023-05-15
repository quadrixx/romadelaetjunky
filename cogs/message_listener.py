from discord.ext import commands


class msg_listener(commands.Cog):
    def __init__(self, bot, list_of_msgs):
        self.bot = bot
        self.lom = list_of_msgs
    #тут
    @commands.Cog.listener()
    async def on_message(self, message):
        if len(self.lom) < 200:


