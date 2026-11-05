import requests, config


def fetch_air_quality(sensors: dict[int, str]) -> list[dict]:
    sensors_hourly = []
    for sensor_id, code in sensors.items():
        resp = requests.get(f"{config.GIOS_URL}{sensor_id}", timeout=config.TIMEOUT)
        resp.raise_for_status()
        print(resp.json()["Lista danych pomiarowych"])
        hourly = [{row["Data"]: row["Wartość"]} for row in resp.json()["Lista danych pomiarowych"]]
        print(hourly)
        break

    return sensors_hourly

if __name__ == "__main__":
    fetch_air_quality(config.GIOS_STATIONS[0]["sensors"])


#TODO: function such as in meteo_client with time in UTC format (ISO text)


