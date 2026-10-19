TIMEOUT = 10
METEO_URL = "https://api.open-meteo.com/v1/forecast"
GIOS_URL = "https://api.gios.gov.pl/pjp-api/v1/rest/data/getData/"
PAST_HOURS = 12

GIOS_STATIONS = [
    {"id": 400,
     "name": "Kraków, Aleja Krasińskiego",
     "sensors": {2746: 'NO', 2747: 'NO2', 2748: 'NOx', 2750: 'PM10', 2752: 'PM2.5'},
     "lat": 50.057678,
     "long": 19.926189
     },
    {"id": 530,
     "name": "Warszawa, Al. Niepodległości",
     "sensors": {3579: 'NO', 3580: 'NO2', 3581: 'NOx', 3584: 'PM10', 3585: 'PM2.5'},
    "lat": 52.219298,
     "long": 21.004724
     },
    {"id": 612,
     "name": "Borsukowizna, Szkółka Leśna",
     "sensors": {4039: 'NO', 4040: 'NO2', 4041: 'NOx', 19657: 'PM10', 19696: 'PM2.5'},
    "lat": 53.215492,
     "long": 23.642153
     }
]
