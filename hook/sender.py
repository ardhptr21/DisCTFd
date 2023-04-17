import aiohttp
from discord import Embed, Webhook

from config import DISCORD_WEBHOOK_URL, NOTIFY_MESSAGE_STYLE


class CTFdSender:
    def parser(self, message, chall_name, chall_category, user_name):
        return message.replace("<category>", chall_category).replace("<name>", chall_name).replace("<username>", user_name)

    async def send(self, **kwargs):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, session=session)
            await webhook.send(**kwargs)
    
    async def send_first_blood(self, chall_name, chall_category, user_name):
        title = self.parser(NOTIFY_MESSAGE_STYLE["FIRST_BLOOD"]["title"], chall_name, chall_category, user_name)
        description = self.parser(NOTIFY_MESSAGE_STYLE["FIRST_BLOOD"]["description"], chall_name, chall_category, user_name)
        embed = Embed(title=title, description=description, color=0xff0000)
        await self.send(embed=embed)

    async def send_solved(self, chall_name, chall_category , user_name):
        title = self.parser(NOTIFY_MESSAGE_STYLE["SOLVED"]["title"], chall_name, chall_category, user_name)
        description = self.parser(NOTIFY_MESSAGE_STYLE["SOLVED"]["description"], chall_name, chall_category, user_name)
        embed = Embed(title=title, description=description, color=0x58a04b)
        await self.send(embed=embed)

sender = CTFdSender()