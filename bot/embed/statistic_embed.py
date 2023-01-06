from discord import Color, Embed


def scoreboard_embed(users):
    for i in users:
        user = users[i]
    
    lists = ""
    for i in users:
        user = users[i]
        if i == "1":
            lists += f"```🥇 {user['name']}\n```"
        elif i == "2":
            lists += f"```🥈 {user['name']}\n```"
        elif i == "3":
            lists += f"```🥉 {user['name']}\n```"
        else:
            lists += f"```#{i} {user['name']}\n```"
    content = f"Top 20 users\n{lists}"

    embed = Embed(
        title="Scoreboard",
        description=content,
        color=Color.blue()
    )
    return embed