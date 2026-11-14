from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def column_name(pollutant: str) -> str:
    return pollutant.lower().replace('.', '')


def gmt_to_utc(gmt_time: str) -> str:
    t = datetime.fromisoformat(gmt_time)
    t = t.replace(tzinfo=timezone.utc)
    return t.isoformat(timespec='minutes')


def local_to_utc(local_time: str) -> str:
    t = datetime.strptime(local_time, "%Y-%m-%d %H:%M:%S")
    t = t.replace(tzinfo=ZoneInfo("Europe/Warsaw"))
    t = t.astimezone(timezone.utc)
    return t.isoformat()


#TODO: zweryfikować czy mam dobry endpoint z open meteo (nie chcę wcześniejszych prognoz tylko rzeczywiste wartości)
#TODO: sformatować funkcje tak żeby zwracały czas w UTC pasujący do formatu DATETIME w mysql i dodać każdej funkcji docstring z opisem
#TODO: dodać mechanizm stronicowania do fetch_air_quality żeby gios_client szybciej chodził
#TODO: sprawdzić czy parametry zgadzają się godzinowo tzn. z jakich godzin robione są średnie itd.
#TODO: zaprojektować bazę danych wstępnie z dwiema tabelami: weather i air_quality, obie z composite primary key
#TODO: dodać kolumny do tabel i dopisać w jakiś sposób jednostki
