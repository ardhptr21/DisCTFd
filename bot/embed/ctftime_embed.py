from discord import Embed, Color
from datetime import datetime

from utils.time import parseISOTime


def events_embed(events, timezone):
    content = f'{timezone}\n\n'
    for event in events:
        if event['onsite']:
            continue
        current = f"**{event['title']}**\n"
        current += f"Start: {parseISOTime(event['start'])}\n"
        current += f"Finish: {parseISOTime(event['finish'])}\n"
        current += f"Duration: {event['duration']['days']} days, {event['duration']['hours']} hours"
        content += current + '\n\n'
    embed = Embed(title="CTFTime events",
                  description=content, color=Color.red())
    return embed
