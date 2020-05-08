import requests
from pathlib import Path
import csv
import urllib.request

ELENCO_NOMI = [
    "abruzzo",
    "basilicata",
    "calabria",
    "campania",
    "emilia",
    "friuli",
    "lazio",
    "liguria",
    "lombardia",
    "marche",
    "molise",
    "piemonte",
    "puglia",
    "sardegna",
    "sicilia",
    "toscana",
    "trentino",
    "umbria",
    "valle",
    "veneto",
    "Italia",
]


if __name__ == "__main__":
    Path("data").mkdir(parents=True, exist_ok=True)
    for name in ELENCO_NOMI:
        link = f"https://raw.github.com/Gelma/LugMap/master/db/{name}.txt"
        r = requests.get(link, allow_redirects=True)
        open(f"data/{name}.csv", "wb").write(r.content)
