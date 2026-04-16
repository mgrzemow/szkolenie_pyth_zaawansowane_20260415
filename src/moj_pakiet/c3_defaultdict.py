"""
Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Pogrupować adresy email po domenach, jedncześnie pozbywając się duplikatów. Proponuję format:
{
'gmail.com': {'ala@gmail.com', 'ela@gmail.com'}
...
}
3. Zapisujemy adresy email do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   np wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt

Podpowiedzi:
 - nazwę domeny można wyciąć z adresu znajdując znak @
"""

import collections
from pathlib import Path
from pprint import pprint

RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "emaile.txt"


if __name__ == "__main__":
    slownik_rekordow = collections.defaultdict(set)
    with RESOURCE_FILE.open("rt", encoding="utf8") as f:
        for linia in f:
            linia = linia.lower().strip()
            if "@" in linia:
                _, domena = linia.split("@")
                slownik_rekordow[domena].add(linia)
    for domena, emaile in slownik_rekordow.items():
        with (RESOURCE_FILE.parent / f"{domena}.txt").open("wt", encoding="utf8") as f:
            for email in emaile:
                f.write(email + "\n")
