import requests, config, utils


def fetch_air_quality(sensors: dict[int, str], hours_back: int) -> list[dict]:
    """Zwraca listę wierszy (jeden na godzinę, rosnąco po 'time', UTC ISO).
        Każdy wiersz ma wszystkie kolumny zanieczyszczeń; brak pomiaru = None."""
    columns = [utils.column_name(val) for val in sensors.values()]
    hourly = {}

    for sensor_id, pollutant in sensors.items():
        resp = requests.get(f"{config.GIOS_URL}{sensor_id}", timeout=config.TIMEOUT)
        resp.raise_for_status()
        data = resp.json()["Lista danych pomiarowych"]
        col = utils.column_name(pollutant)

        for row in data:
            t = row["Data"]
            if t not in hourly:
                hourly[t] = {"time": t, **dict.fromkeys(columns)}

            hourly[t][col] = row["Wartość"]


    return sorted(list(hourly.values()), key=lambda r: r["time"])

if __name__ == "__main__":
    print(fetch_air_quality(config.GIOS_STATIONS[0]["sensors"], config.PAST_HOURS))



#TODO: dodać obsługę parametru hours_back i zmienić czaś na UTC