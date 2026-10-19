import requests, config


# def fetch_air_quality(sensor_ids: list[int]) -> list[dict]:
#     resp = requests.get(config.GIOS_URL, timeout=config.TIMEOUT)
#
#
#
# if __name__ == "main":
#     print(fetch_sensor_data())


#TODO: function such as in meteo_client with time in UTC format (ISO text)

resp = requests.get("https://api.gios.gov.pl/pjp-api/v1/rest/data/getData/2746")
resp.raise_for_status()

measurements = resp.json()["Lista danych pomiarowych"]

