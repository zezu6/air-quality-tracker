import requests, config
from time_utils import to_utc_iso

HOURLY_VARS = [
    "temperature_2m",
    "relative_humidity_2m",
    "wind_speed_10m",
    "wind_direction_10m",
    "precipitation",
    "surface_pressure",
    "boundary_layer_height"
]


def fetch_weather(lat: float, long: float, hours_back: int) -> list[dict]:
    """Pobiera pomiary z ostatnich `hours_back` godzin.

    Zwraca listę słowników, w których `time` jest w formacie ISO z '+00:00'.
    """
    params = {
        "latitude": lat,
        "longitude": long,
        "hourly": HOURLY_VARS,
        "forecast_hours": 0,
        "past_hours": hours_back,
        "timezone": "GMT"
    }
    resp = requests.get(config.METEO_URL, params=params, timeout=config.TIMEOUT)
    resp.raise_for_status()

    hourly = resp.json()["hourly"]
    measurements = [{key: hourly[key][i] for key in hourly.keys()} for i in range(len(hourly["time"]))]
    for row in measurements:
        row["time"] = to_utc_iso(row["time"])

    return measurements


if __name__ == "__main__":
    for station in config.GIOS_STATIONS:
        print(fetch_weather(station["lat"], station["long"], config.PAST_HOURS))

