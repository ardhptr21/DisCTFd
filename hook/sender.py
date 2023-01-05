import aiohttp
from discord import Embed, Webhook

from config import WEBHOOK_URL


class CTFdSender:
    async def send(self, **kwargs):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(WEBHOOK_URL, session=session)
            await webhook.send(**kwargs)
    
    async def send_first_blood(self, chall_name, chall_category, user_name):
        embed = Embed(title="🩸 First Blood", description=f"`{chall_category}: {chall_name}` has been pwned by `{user_name}`", color=0xff0000)
        embed.set_image(url="https://media.tenor.com/MLkx8VkaXqUAAAAC/rambo-first-blood.gif")
        await self.send(embed=embed)

    async def send_solved(self, chall_name, chall_category , user_name):
        embed = Embed(title="✅ Challenge Solved", description=f"`{chall_category}: {chall_name}` has been solved by `{user_name}`", color=0x58a04b)
        await self.send(embed=embed)

sender = CTFdSender()