from discord.ext import commands

from .embed.help_embed import help_bot_embed
from .handlers.checkflag_handler import docstring as checkflag_docstring
from discord import Embed, Color

class CTFdBotHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping: dict[commands.Cog | None, list[commands.Command | None]]) -> None:
        embed = help_bot_embed(mapping)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command: commands.Command) -> None:
        embed = Embed(title=f"${command.name}", description=command.help, color=Color.blue())
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def command_not_found(self, string: str) -> str:
        if string == "checkflag":
            embed = Embed(title=f"${string}", description=checkflag_docstring, color=Color.blue())
            embed.set_footer(text="Please send message directly to the bot")
            await self.context.send(embed=embed)
            return "custom_found_command"
        return super().command_not_found(string)
    
    async def send_error_message(self, error: str) -> None:
        if error == "custom_found_command": return
        await super().send_error_message(error)