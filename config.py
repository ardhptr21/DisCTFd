from dotenv.main import load_dotenv
import os

load_dotenv()

"""
Config

This is the main config for the bot and the webhook.
"""

DEBUG = os.getenv("DEBUG", 'True') == 'True'
TIMEZONE = os.getenv("TIMEZONE", 'Asia/Jakarta')
SLEEP_TIME = int(os.getenv("SLEEP_TIME", 10)) # seconds
# This is the option what runner do you want to run
RUNNER = {
    "BOT": os.getenv("RUNNER_BOT", 'True') == 'True',
    "WEBHOOK": os.getenv("RUNNER_WEBHOOK", 'True') == 'True'
}
ONLY_FIRST_BLOOD = os.getenv("ONLY_FIRST_BLOOD", 'False') == 'True'

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", 'https://discord.com/api/webhooks/...')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", '...')

HOST = os.getenv("HOST", 'https://ctfd.example.com')
TOKEN = os.getenv("TOKEN", '...')

DB_CREDENTIALS = {
    "host": os.getenv("DB_HOST", 'db'),
    "user": os.getenv("DB_USER", 'disctfd'),
    "password": os.getenv("DB_PASSWORD", 'disctfd'),
    "database": os.getenv("DB_DATABASE", 'disctfd')
}

"""
Template:
<category> = category of the challenge
<name> = name of the challenge
<username> = username of the solver

Note: The description is support discord markdown
"""
NOTIFY_MESSAGE_STYLE = {
    "FIRST_BLOOD": {
        "title": ":drop_of_blood: First Blood",
        "description": "`<name>` has been pwned by `<username>`",
    },
    "SOLVED": {
        "title": ":white_check_mark: Challenge Solved",
        "description": "`<name>` has been solved by `<username>`",
    },
}
