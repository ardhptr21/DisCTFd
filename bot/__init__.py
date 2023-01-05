import discord


from .bot import CTFdBot
from config import DISCORD_TOKEN

def init():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = CTFdBot(intents=intents, command_prefix="$")

    bot.run(token=DISCORD_TOKEN)