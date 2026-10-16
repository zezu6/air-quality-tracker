import requests

GIOS_SENSORS_URL = "https://api.gios.gov.pl/pjp-api/v1/rest/station/sensors"
IDS = [400, 530, 612]

for station_id in IDS:
    r = requests.get(f"{GIOS_SENSORS_URL}/{station_id}", params={"size": 500}, timeout=5)
    r.raise_for_status()

    sensors = r.json()["Lista stanowisk pomiarowych dla podanej stacji"]
    station_sensors = {s["Identyfikator stanowiska"]: s["Wskaźnik - kod"] for s in sensors}
    print(station_id, station_sensors)



