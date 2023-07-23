import discord
from discord.ext import commands
from vidstream import AudioReceiver
from vidstream import AudioSender
import threading


sender = AudioSender('192.168.0.108', 9999)
reciever = AudioReceiver('', 9999)
recieve_thread = threading.Thread(target=reciever.start_server)
send_thread = threading.Thread(target=sender.start_stream)


class Soul(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def zxc(self, ctx):
        channel = await self.bot.fetch_channel('830124399369126002')
        vc = channel.connect()
        await vc.play(source=discord.AudioSource.read())


