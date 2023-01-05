import logging

from discord.ext import commands
from discord import Embed
from requests import RequestException
from json.decoder import JSONDecodeError

from .templates.embed import challs_embed, scoreboard_embed

from utils.session import session as s

class CTFdBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_commands()

    async def on_ready(self):
        print("Bot is ready")

    def add_commands(self):
        @self.command(name="challenges")
        async def challs(ctx):
            try:
                challs = s.get("/challenges").json()["data"]
                await ctx.send(embed=challs_embed(self.user, challs))
            except (RequestException, JSONDecodeError, KeyError) as e:
                logging.error(e)
                await ctx.send("Error occured")
        
        @self.command(name="scoreboard")
        async def scoreboard(ctx):
            try:
                scoreboard = s.get("/scoreboard").json()["data"]
                await ctx.send(embed=scoreboard_embed(self.user, scoreboard))
            except (RequestException, JSONDecodeError, KeyError) as e:
                logging.error(e)
                await ctx.send("Error occured")
