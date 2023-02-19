from discord import Embed, Color

from utils.time import parseISOTime


def events_embed(events, timezone):
    content = f'{timezone}\n\n'
    for event in events:
        if event['onsite']:
            continue
        current = f"**{event['title']}**\n"
        current += f"Start: {parseISOTime(event['start'])}\n"
        current += f"Finish: {parseISOTime(event['finish'])}\n"
        current += f"Duration: {event['duration']['days']} days, {event['duration']['hours']} hours\n"
        current += f"Format: {event['format']}\n"
        current += f"Url: {event['url']}\n"
        current += f"CTFTime Url: {event['ctftime_url']}\n"
        content += current + '\n\n'
    embed = Embed(title="CTFTime events",
                  description=content, color=Color.red())
    return embed
