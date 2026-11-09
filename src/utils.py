from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def to_utc_iso(gmt_time: str) -> str:
    t = datetime.fromisoformat(gmt_time)
    t = t.replace(tzinfo=timezone.utc)
    return t.isoformat(timespec='minutes')


def column_name(pollutant: str) -> str:
    return pollutant.lower().replace('.', '')


def local_to_utc_iso(time: str) -> str:
    t = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    t = t.replace(tzinfo=ZoneInfo("Europe/Warsaw"))
    t = t.astimezone(timezone.utc)
    return t.isoformat()


