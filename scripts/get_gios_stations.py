import requests

GIOS_STATIONS_URL = "https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll"
IDS = [400, 530, 612]

r = requests.get(GIOS_STATIONS_URL, params={"size": 500}, timeout=5)
r.raise_for_status()
stations_list = r.json()["Lista stacji pomiarowych"]

for station in stations_list:
    if station["Identyfikator stacji"] in IDS:
        print(station)

