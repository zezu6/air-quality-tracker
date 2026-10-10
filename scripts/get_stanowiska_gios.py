import requests

STANOWISKA_GIOS_URL = "https://api.gios.gov.pl/pjp-api/v1/rest/station/sensors"
IDS = [400, 530, 612]

for id_stacji in IDS:
    resp = requests.get(f"{STANOWISKA_GIOS_URL}/{id_stacji}", params={"size": 500}, timeout=5)
    resp.raise_for_status()

    stanowiska = resp.json()["Lista stanowisk pomiarowych dla podanej stacji"]
    stanowiska_stacji = {s["Identyfikator stanowiska"]: s["Wskaźnik - kod"] for s in stanowiska}
    print(id_stacji, stanowiska_stacji)



