import logging
import asyncio

from bot import CTFdBot
from db import CTFdDB
from sender import sender

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    handler = logging.FileHandler("./log/ctfd_bot.log")
    handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(handler)

    logging.info("Starting CTFdBot")

    bot = CTFdBot()

    CTFdDB.init_db()

    loop = asyncio.new_event_loop()
    loop.create_task(bot.run())
    
    try:
        loop.run_forever()
    except:
        loop.stop()
        loop.close()