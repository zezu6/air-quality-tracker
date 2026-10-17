import requests, config


def fetch_weather(lat: float, long: float) -> list[dict]: # function returns time in UTC format
    params = {
        "latitude": lat,
        "longitude": long,
        "hourly": ["temperature_2m",
                   "relative_humidity_2m",
                   "wind_speed_10m",
                   "wind_direction_10m",
                   "precipitation",
                   "surface_pressure",
                   "boundary_layer_height"],
        "forecast_hours": 0,
        "past_hours": config.PAST_HOURS,
        "timezone": "GMT"
    }
    resp = requests.get(config.METEO_URL, params=params, timeout=config.TIMEOUT)
    resp.raise_for_status()
    measurements = resp.json()["hourly"]
    measurements = [{key: measurements[key][i] for key in measurements.keys()} for i in range(len(measurements["time"]))]
    return measurements


if __name__ == "__main__":
    for station in config.GIOS_STATIONS:
        print(fetch_weather(lat=station["lat"], long=station["long"]))

#TODO: change time format for ISO text
