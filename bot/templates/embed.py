from discord import Embed, ClientUser

def challs_embed(user: ClientUser, challs) -> Embed:
    categories = list(set([chall["category"] for chall in challs]))

    embed = Embed(title="Challenges", description="List all challenges", color=0x00ff00)
    
    for category in categories:
        content = ""
        for idx, chall in enumerate(challs):
            if chall["category"] == category:
                content += f'{idx + 1}. {chall["name"]}\n'
        content = f"```{content}```"
        embed.add_field(name=category, value=content, inline=False)

    return embed

def scoreboard_embed(user: ClientUser, scoreboard) -> Embed:
    content = ""
    for idx, user in enumerate(scoreboard):
        content += f'#{idx + 1}. {user["name"]} - {user["score"]}\n'
    content = f"List top 10 users in scoreboard\n```{content}```"
    embed = Embed(title="Scoreboard", description=content, color=0x00ff00)
    return embed