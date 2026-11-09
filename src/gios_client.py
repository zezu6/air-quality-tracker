import requests, config, src.utils


def fetch_air_quality(sensors: dict[int, str], hours_back: int) -> list[dict]:
    """Zwraca listę wierszy (jeden na godzinę, rosnąco po 'time', UTC ISO).
        Każdy wiersz ma wszystkie kolumny zanieczyszczeń; brak pomiaru = None."""
    columns = [src.utils.column_name(val) for val in sensors.values()]
    hourly = {}

    for sensor_id, pollutant in sensors.items():
        resp = requests.get(f"{config.GIOS_URL}{sensor_id}", timeout=config.TIMEOUT)
        resp.raise_for_status()
        data = resp.json()["Lista danych pomiarowych"]
        col = src.utils.column_name(pollutant)

        for row in data:
            t = src.utils.local_to_utc_iso(row["Data"])
            if t not in hourly:
                hourly[t] = {"time": t, **dict.fromkeys(columns)}

            hourly[t][col] = row["Wartość"]

    sensors_hourly = sorted(hourly.values(), key=lambda r: r["time"])[-hours_back:]
    return sensors_hourly

if __name__ == "__main__":
    print(fetch_air_quality(config.GIOS_STATIONS[0]["sensors"], config.PAST_HOURS))

