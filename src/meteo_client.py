import requests, config


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


def fetch_weather(latitude: float, longitude: float, ) -> dict:
    # get measurements for the last 12 hours
    pass


resp = requests.get(config.METEO_URL, params=params, timeout=config.TIMEOUT)
measurements = resp.json()["hourly"]

print(measurements["time"])
for k in measurements.keys():
    print(k, len(measurements[k]))


#TODO: napisać funkcję przyjmującą współrzędne i liczbę godzin wstecz
#TODO: ogarnąć jednolity czas dla pomiarów z GIOŚ i Meteo
