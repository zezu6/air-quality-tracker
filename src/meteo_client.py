import requests, config


def fetch_weather(latitude: float, longitude: float, ) -> dict:
    pass


params = {
    "latitude": config.GIOS_STATIONS[1]["lat"],
    "longitude": config.GIOS_STATIONS[1]["long"],
    "hourly": ["temperature_2m",
               "relative_humidity_2m",
               "wind_speed_10m",
               "wind_direction_10m",
               "precipitation",
               "surface_pressure",
               "boundary_layer_height"],
    "timezone": "GMT"
}

resp = requests.get(config.METEO_URL, params=params, timeout=config.TIMEOUT)
measurements = resp.json()["hourly"]

print(measurements["time"])
for k in measurements.keys():
    print(k, len(measurements[k]))


#TODO: napisać funkcję przyjmującą współrzędne i liczbę godzin wstecz
#TODO: ogarnąć jednolity czas dla pomiarów z GIOŚ i Meteo
#TODO: przetłumaczyć cały kod na angielski
