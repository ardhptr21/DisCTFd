import logging
from json.decoder import JSONDecodeError

from discord.ext import commands
from requests import RequestException

from utils.session import session as s

from ..embed.challs_embed import chall_embed, list_challs_embed


class Challenges(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="challs")
    async def challs(self, ctx):
        try:
            challs = s.get("/challenges").json()["data"]
            await ctx.send(embed=list_challs_embed(challs))
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
            await ctx.send("Error occured")

    @commands.command(name="chall")
    async def chall(self, ctx, chall_id: int):
        try:
            res = s.get(f"/challenges/{chall_id}")
            if res.status_code == 404:
                await ctx.send("Challenge not found")
                return
                
            chall = res.json()["data"]
            await ctx.send(embed=chall_embed(chall))
        except (RequestException, JSONDecodeError, KeyError) as e:
            logging.error(e)
