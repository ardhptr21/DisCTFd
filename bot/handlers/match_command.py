from discord import Message
import re

from .checkflag_handler import check_flag_handler

async def match_command_handler(prefix: str, message: Message):
    command = re.search(f"^\{prefix}\w+", message.content)
    if not command: return await message.channel.send("Sorry, you typed something wrong")
    command = command.group(0)
    match command.replace(prefix, ""):
        case "checkflag":
            await check_flag_handler(message)
        case _:
            await message.channel.send("Command not found")