import logging
import os
from threading import Thread

from config import RUNNER
from bot import init as bot_init
from hook import init as hook_init

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    if os.path.exists("disctfd.log"): os.remove("disctfd.log")
    open("disctfd.log", "a").close()

    handler = logging.FileHandler("disctfd.log")
    handler.setLevel(logging.DEBUG)
    
    logging.getLogger().addHandler(handler)

    if RUNNER['BOT'] and RUNNER['WEBHOOK']:
        t1 = Thread(target=hook_init)
        t2 = Thread(target=bot_init)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    
    if RUNNER['BOT']:
        bot_init()
    elif RUNNER['WEBHOOK']:
        hook_init()
    else:
        logging.error("No runner selected.")
        exit(1)