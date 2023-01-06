from urllib.parse import quote, urljoin

from discord import Colour, Embed

from config import HOST


def list_challs_embed(challs) -> Embed:
    categories = list(set([chall["category"] for chall in challs]))
    description = f"List for all available challenges\n\n*Output format*: ```ansi\n[1;2m<name> - [1;31m<id>[0m[0m```"
    embed = Embed(title="Challenges", description=description, color=Colour.blue())
    
    for category in categories:
        content = ""
        count = dict.fromkeys(categories, 1)
        for chall in challs:
            if chall["category"] == category:
                content += f"```ansi\n[1;2m{chall['name']} - [1;31m{chall['id']}[0m[0m```"
                count[chall["category"]] += 1
        
        embed.add_field(name=category, value=content, inline=False)
    del content
    return embed

def chall_embed(chall) -> Embed:
    embed = Embed(title=chall["name"], description=chall["description"], color=Colour.blue())
    embed.add_field(name="Category", value=chall["category"], inline=False)
    embed.add_field(name="Point", value=chall["value"], inline=False)
    embed.add_field(name="Solves", value=chall["solves"], inline=False)
    embed.add_field(name="ID", value=chall["id"], inline=False)

    path = '/challenges#' + quote(f'{chall["name"]}-{chall["id"]}')
    link = urljoin(HOST, path)
    embed.add_field(name="Link", value=f"[Visit Challenge]({link})", inline=False)
    return embed