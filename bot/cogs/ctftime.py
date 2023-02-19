import logging
from json.decoder import JSONDecodeError
from datetime import datetime
import math

from discord.ext import commands
import requests
import pytz

from config import TIMEZONE
from ..embed.ctftime_embed import events_embed


class CTFTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://ctftime.org/api/v1"
        self.local_timezone = pytz.timezone(TIMEZONE)
        self.gmt_offset = math.floor(self.local_timezone.utcoffset(
            datetime.now()).total_seconds() / 3600)
        print(self.gmt_offset)

    @commands.command(name="events")
    async def events(self, ctx):
        """
        List all events from CTFTime

        **Usage:** `$events`
        """
        try:
            events = requests.get(
                f"{self.base_url}/events/?limit=10", headers={"User-Agent": "DisCTFd"}).json()
            await ctx.send(embed=events_embed(events, f"{self.local_timezone} GMT {self.gmt_offset:+d}"))
        except (JSONDecodeError, requests.RequestException, KeyError) as e:
            logging.error(e)
            await ctx.send("Error occured")
