from discord.ext import commands


class msg_listener(commands.Cog):
    def __init__(self, bot, list_of_msgs):
        self.bot = bot
        self.lom = list_of_msgs
        self.ready = False
    #тут делаем счетчик сообщений
    @commands.Cog.listener()
    async def on_message(self, message):
        if len(self.lom) < 20:
            self.lom.append(message.content)
        else:
            self.ready = True






