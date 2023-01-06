import discord
from discord.ext import commands

from config import DISCORD_TOKEN

from .cogs.challenges import Challenges
from .cogs.statistic import Statistic
from .help import CTFdBotHelp

def init():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="$", intents=intents, help_command=CTFdBotHelp())

    @bot.event
    async def on_ready():
        await bot.add_cog(Challenges(bot))
        await bot.add_cog(Statistic(bot))
        print(f"Logged in as {bot.user}")

    bot.run(token=DISCORD_TOKEN)