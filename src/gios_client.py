import requests, config


# def fetch_air_quality(sensor_ids: list[int]) -> list[dict]:
#     for s_id in sensor_ids:
#         resp = requests.get(f"{config.GIOS_URL}{s_id}", timeout=config.TIMEOUT)
#         resp.raise_for_status()
#         sensor_data = resp.json()["Lista danych pomiarowych"]
#
#
#
# if __name__ == "main":
#     print(fetch_air_quality(config.GIOS_STATIONS[0]["sensors"]))


#TODO: function such as in meteo_client with time in UTC format (ISO text)

resp = requests.get(f"{config.GIOS_URL}{2746}", timeout=config.TIMEOUT)
resp.raise_for_status()
sensor_data = resp.json()["Lista danych pomiarowych"]
print(sensor_data)
