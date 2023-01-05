import asyncio
from .hook import CTFdHook

def init():
    hook = CTFdHook()

    loop = asyncio.new_event_loop()
    loop.create_task(hook.run())

    try:
        loop.run_forever()
    except:
        loop.stop()
        loop.close()