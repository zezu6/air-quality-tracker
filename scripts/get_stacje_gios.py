import requests

STACJE_GIOS_URL = "https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll"
IDS = [400, 530, 612]

odp = requests.get(STACJE_GIOS_URL, params={"size": 500}, timeout=5)
odp.raise_for_status()
lista_stacji = odp.json()["Lista stacji pomiarowych"]

for stacja in lista_stacji:
    if stacja["Identyfikator stacji"] in IDS:
        print(stacja)

