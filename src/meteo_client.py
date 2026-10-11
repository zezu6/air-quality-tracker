import requests, config

params = {
    "latitude": config.STACJE_GIOS[1]["lat"],
    "longitude": config.STACJE_GIOS[1]["long"],
    "hourly": ["temperature_2m",
               "relative_humidity_2m",
               "wind_speed_10m",
               "wind_direction_10m",
               "precipitation",
               "surface_pressure",
               "boundary_layer_height"],
    "timezone": "GMT"
}

resp = requests.get(config.METEO_URL, params=params)
pomiary = resp.json()["hourly"]

print(pomiary["time"])
for k in pomiary.keys():
    print(k, len(pomiary[k]))


#TODO: ogarnąć jednolity czas dla pomiarów z GIOŚ i Meteo
