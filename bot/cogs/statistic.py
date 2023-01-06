import logging
from json.decoder import JSONDecodeError

from discord.ext import commands
from requests import RequestException

from utils.session import session as s

from ..embed.statistic_embed import scoreboard_embed


class Statistic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="scoreboard")
    async def scoreboard(self, ctx):
        """
        Shows top 20 users in scoreboard

        **Usage:** `$scoreboard`
        """
        try:
            users = s.get("/scoreboard/top/20").json()['data']
            await ctx.send(embed=scoreboard_embed(users))
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            await ctx.send("Error occured")