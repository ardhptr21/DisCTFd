from discord import Webhook
import aiohttp

from config import WEBHOOK_URL

class CTFdSender:
    async def send(self, **kwargs):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(WEBHOOK_URL, session=session)
            await webhook.send(**kwargs)

sender = CTFdSender()