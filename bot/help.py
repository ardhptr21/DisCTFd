from discord.ext import commands

from .embed.help_embed import help_bot_embed
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