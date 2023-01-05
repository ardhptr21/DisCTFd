import logging
import os

from hook import init as hook_init

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    if os.path.exists("disctfd.log"): os.remove("disctfd.log")
    open("disctfd.log", "a").close()

    handler = logging.FileHandler("disctfd.log")
    handler.setLevel(logging.DEBUG)
    
    logging.getLogger().addHandler(handler)

    hook_init()