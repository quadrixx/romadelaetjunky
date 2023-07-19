import discord
from discord.ext import commands


class Handshaking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        textchennel = await self.bot.fetch_channel('1118168172995027015')
        if before.channel is None and after.channel:
            channel = after.channel
            view = discord.ui.View()
            members = channel.members
            members.remove(member)
            if len(members) > 0:
                for i in members:
                    view.add_item(Button(i.name))
                await textchennel.send(view=view)

    @commands.command()
    async def do(self, ctx):
        guild = self.bot.get_guild(426816847254519808)
        channel = discord.utils.get(guild.channels, name='няwимся')
        await channel.connect()
        print(channel)


class Button(discord.ui.Button):
    def __init__(self, username):
        super().__init__(label=username, style=discord.ButtonStyle.red)

    async def callback(self, interaction):
        self.style = discord.ButtonStyle.green
        self.disabled = True
        self.label = 'заебись'
        await interaction.response.edit_message(view=self.view)


def setup(bot):
    bot.add_cog(Handshaking(bot))
