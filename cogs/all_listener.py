from discord.ext import commands
from Demotivor import Demotivator
import random
class msg_listener(commands.Cog):
    def __init__(self, bot, list_of_msgs,list_of_urls):
        self.bot = bot
        self.lom = list_of_msgs
        self.lou = list_of_urls
        self.ready_for_msgs = False
        self.ready_for_urls = False
        self.obj = Static(self.ready_for_msgs, self.ready_for_urls, self.lom, self.lou)
    #тут делаем счетчик сообщений
    @commands.Cog.listener()
    async def on_message(self, message):
        if len(self.lom) < 10 and message.content != "":
            self.lom.append(message.content)
        elif message.content == "":
            pass
        else:
            self.ready_for_msgs = True
        attachments = message.attachments
        if len(attachments) != 0:
            self.ready_for_urls = True
            for att in attachments:
                self.lou.append(att.url)
        self.obj.update(self.ready_for_msgs, self.ready_for_urls, self.lom, self.lou)

class Static:
    def __init__(self, msg_rdy: bool, url_rdy: bool, lom, lou):
        self.msg_rdy = msg_rdy
        self.url_rdy = url_rdy
        self.lom = lom
        self.lou = lou

    def update(self, msg, url, lom, lou):
        self.msg_rdy = msg
        self.url_rdy = url
        self.lom = lom
        self.lou = lou
        print(self.msg_rdy)
        print(self.lom)
        if self.msg_rdy == True and self.url_rdy == True:
            print(self.lom)
            print(self.lou)
            self.create_demo(self.shuffle(self.lom, self.lou))

    def create_demo(self, lst):
        dem = Demotivator(*lst)

    def shuffle(self, lom: list, lou: list) -> list:
        for_dem = []
        for i in range(2):
            a = random.randint(0, len(lom)-1)
            for_dem.append(lom[a])
        a = random.randint(0, len(lou)-1)
        for_dem.append(lou[a])
        return for_dem
def setup(bot):
    bot.add_cog(msg_listener(bot,[],[]))









