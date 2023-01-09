"""
Config

This is the main config for the bot and the webhook.

!PLEASE DO NOT TYPE <> IN YOUR OWN CONFIGURATION!
"""

# This is the webhook url for the discord server to broadcast first blood and solved message
DISCORD_WEBHOOK_URL = "<discord webhook url>"

# This is the bot discord application token
DISCORD_TOKEN = "<discord bot token>"

# This is the host of your CTFd instance/platform
HOST = "<base url to your ctfd platform"

# This is the token admin that you generated from your CTFd instance/platform
TOKEN = "<token or secret key on your ctfd platform>"

# This is the sleep time of fetching a solver from the CTFd instance/platform
SLEEP_TIME = 10 # in seconds

# This is the credentials for the database, using MYSQL
DB_CREDENTIALS = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "disctfd",
}

"""
If you use docker, please use this instead

DB_CREDENTIALS = {
    "host": "db",
    "user": "disctfd",
    "password": "disctfd",
    "database": "disctfd",
}
"""

# This is the option what runner do you want to run
RUNNER = {
    "BOT": True,
    "WEBHOOK": True,
}