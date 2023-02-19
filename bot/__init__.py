import discord
from discord.ext import commands

from config import DISCORD_TOKEN

from .cogs.challenges import Challenges
from .cogs.statistic import Statistic
from .cogs.ctftime import CTFTime
from .help import CTFdBotHelp
from .handlers.match_command import match_command_handler


def init():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="$", intents=intents,
                       help_command=CTFdBotHelp())

    @bot.event
    async def on_ready():
        await bot.add_cog(Challenges(bot))
        await bot.add_cog(Statistic(bot))
        await bot.add_cog(CTFTime(bot))
        await bot.change_presence(activity=discord.Game(name="$help"))
        print(f"Logged in as {bot.user}")

    @bot.event
    async def on_message(message: discord.Message):
        if isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user:
            await match_command_handler(bot.command_prefix, message)
        else:
            await bot.process_commands(message)

    bot.run(token=DISCORD_TOKEN)
