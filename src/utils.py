from datetime import datetime, timezone


def to_utc_iso(gmt_time: str) -> str:
    t = datetime.fromisoformat(gmt_time)
    t = t.replace(tzinfo=timezone.utc)
    return t.isoformat(timespec='minutes')


def column_name(name: str) -> str:
    return name.lower().replace('.', '')


