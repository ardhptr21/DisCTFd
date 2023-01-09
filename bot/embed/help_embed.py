from discord.ext.commands import Cog, Command
from discord import Embed, Color

how_use = """```ansi
[2;34m[1;34mcommand prefix[0m[2;34m[0m[2;34m:[0m [2;32m$[0m
[2;34m[1;34mexample[0m[2;34m[0m[2;34m:[0m [2;32m$challs[0m
Do [2;31m[1;31mNOT[0m[2;31m[0m type [2;33m<>[0m when using commands!
```"""

def help_bot_embed(mapping: dict[Cog | None, list[Command | None]]) -> Embed: 
    embed = Embed(title="Help", description=how_use, color=Color.blue())
    embed.set_footer(text="$help <command> for more info on a command.")

    for cog, cmds in mapping.items():
        content = "".join([f"\n{cmd.name}" for cmd in cmds])
        content = f"```{content}```\n"
        embed.add_field(
            name = cog.qualified_name if cog else "Others",
            value = content,
        )
    embed.add_field(name="Direct Message", value="```$checkflag```")

    return embed