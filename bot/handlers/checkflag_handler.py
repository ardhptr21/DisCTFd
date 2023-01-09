import re
import logging
from json import JSONDecodeError

from discord import Message
from requests import RequestException

from utils.session import session as s


async def check_flag_handler(message: Message):
    """
    To check the flag is correct or wrong

    **Usage:** `$checkflag id:<chall_id> flag:<flag>`

    **Example:**
    ```ansi
[2;32m$checkflag[0m [2;34mid[0m:[2;31m7[0m [2;34mflag[0m:[2;31mSTEMBACTF{flag_checker_is_useful}[0m```
    """
    chall_id = re.search("id:(\d+)", message.content)
    if not chall_id: return await message.channel.send("Please specify the challenge id")
    chall_id = chall_id.group(1)

    flag = re.search("flag:(.+)", message.content)
    if not flag: return await message.channel.send("Please specify the flag")
    flag = flag.group(1)
    
    try:
        data = s.get(f"challenges/{chall_id}/flags").json()['data']
        if not data: return await message.channel.send(f"Challenge with id {chall_id} is not found")
        server_flag = data[0]['content']

        if server_flag != flag:
            await message.channel.send("❌ Wrong flag")
        else:
            await message.channel.send("✅ Correct flag")
    except (RequestException, JSONDecodeError, KeyError) as e:
        logging.error(e)
        await message.channel.send("❌ Something went wrong")

docstring = check_flag_handler.__doc__