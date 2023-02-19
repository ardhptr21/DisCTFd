from datetime import datetime
import pytz

from config import TIMEZONE


def parseISOTime(time: str, format: str = "%Y-%m-%d %H:%M"):
    local_timezone = pytz.timezone(TIMEZONE)
    date = datetime.fromisoformat(time).astimezone(local_timezone)
    dateformat = date.strftime(format)

    return dateformat
