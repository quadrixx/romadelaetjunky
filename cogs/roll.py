import discord
from discord.ext import commands
from random import randint


class roll(commands.Cog):

    @commands.slash_command(name='roll')
    async def roll(self, ctx):
        number = randint(0, 100)
        await ctx.respond("{} получает случайное число (1-100): {}".format(ctx.user.name, number))


def setup(bot):
    bot.add_cog(roll(bot))
