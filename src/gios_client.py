import requests, config
from src.utils import column_name, local_to_utc


def fetch_air_quality(sensors: dict[int, str], hours_back: int = config.PAST_HOURS) -> list[dict]:
    columns = [column_name(val) for val in sensors.values()]
    hourly = {}

    for sensor_id, pollutant in sensors.items():
        resp = requests.get(f"{config.GIOS_URL}{sensor_id}", timeout=config.TIMEOUT)
        resp.raise_for_status()
        data = resp.json()["Lista danych pomiarowych"]
        col = column_name(pollutant)

        for row in data:
            t = local_to_utc(row["Data"])
            if t not in hourly:
                hourly[t] = {"time": t, **dict.fromkeys(columns)}

            hourly[t][col] = row["Wartość"]

    sensors_hourly = sorted(hourly.values(), key=lambda r: r["time"])[-hours_back:]
    return sensors_hourly


if __name__ == "__main__":
    for station in config.GIOS_STATIONS:
        print(fetch_air_quality(station["sensors"]))

