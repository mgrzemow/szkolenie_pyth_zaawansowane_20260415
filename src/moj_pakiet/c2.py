"""
# Ćwiczenie:

Napisać program, który:

1. Wczytuje z pliku tekstowego dane:
   - nazwa towaru
   - ilość towaru
   - jednostka miary
   - cena

Plik jest w formacie:

```text
Banany 2.4 kg 3.5
Kiwi 3 szt 2.3
Piwo 4 szt 2.4
Kiwi 3 szt 2.3
Kiwi 4.5 kg 11.5
```

2. Po każdym towarze program dodaje dane do listy zakupów w formacie:

```python
[
['chleb', 3, 'szt', 4.6],
['cebula', 1.55, 'kg', 2.5]
]
```

3. Używając danych z listy stworzonej w pkt 2 wypisuje na ekran paragon w formie:

```text
Pietruszka  2.0 kg x 4.60     9.20
Banany      3.0 kg x  3.5    10.50
----------------------------------
SUMA:                        19.70
```

Kolumny mają mieć szerokości:

- nazwa - 12 znaków,
- ilość - 2 znaki przed kropką i 2 po
- jednostka miary - 4 znaki
- cena - 3 znaki przed kropką i 2 po
- wartość pozycji - 5 znaków przed kropką i 2 po
- SUMA - 7 znaków przed kropką i 2 po

## Podpowiedzi:

- pętla for
- formatowanie f-stringow
"""

from pathlib import Path
from pprint import pprint


RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "towary.txt"


def wczytaj_towary(plik_towary: Path = RESOURCE_FILE) -> list[tuple[str, float, str, float]]:
    """Wczytuje dane o towarach z pliku tekstowego do listy rekordow.

    Funkcja czyta plik linia po linii i pomija:

    - puste wiersze,
    - linie zaczynajace sie od ``#``.

    Kazdy poprawny wiersz jest interpretowany jako rekord w formacie
    ``nazwa ilosc jednostka cena`` i zamieniany na krotke:
    ``(towar, ilosc, jednostka_miary, cena)``.

    Args:
        plik_towary: Sciezka do pliku z danymi o towarach.

    Returns:
        Lista rekordow odczytanych z pliku. Kazdy rekord ma postac
        ``(nazwa_towaru, ilosc, jednostka_miary, cena)``.

    Raises:
        FileNotFoundError: Gdy wskazany plik nie istnieje.
        ValueError: Gdy liczby w pliku nie dadza sie przekonwertowac do typu
            ``float``.
    """
    lista_rekordow: list[tuple[str, float, str, float]] = []

    with plik_towary.open("rt", encoding="utf8") as f:
        for linia in f:
            # Pomijamy puste linie i komentarze, aby czytac tylko dane.
            if linia.strip() and not linia.strip().startswith('#'):
                towar, ilosc, jm, cena, *_ = linia.split()
                ilosc_float = float(ilosc.strip("'"))
                cena_float = float(cena.strip("'"))
                rekord = (towar, ilosc_float, jm, cena_float)
                lista_rekordow.append(rekord)

    return lista_rekordow


def stworz_paragon(lista_rekordow: list[tuple[str, float, str, float]]) -> str:
    """Tworzy tekstowa reprezentacje paragonu na podstawie listy rekordow.

    Funkcja iteruje po rekordach odczytanych z pliku i buduje wielowierszowy
    napis zawierajacy:

    - nazwe towaru,
    - ilosc,
    - jednostke miary,
    - cene jednostkowa,
    - wartosc pozycji.

    Na koncu dodawana jest linia oddzielajaca oraz laczna suma wszystkich
    pozycji z paragonu.

    Args:
        lista_rekordow: Lista rekordow w formacie
            ``(nazwa_towaru, ilosc, jednostka_miary, cena)``.

    Returns:
        Napis reprezentujacy paragon gotowy do wypisania na ekran.
    """
    paragon = ''
    suma = 0.0

    for towar, ilosc, jm, cena in lista_rekordow:
        # Dla kazdej pozycji obliczamy wartosc czastkowa i aktualizujemy sume.
        wartosc = round(ilosc * cena, 2)
        suma = round(suma + wartosc, 2)
        paragon += f'{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n'

    paragon += '-' * 41 + '\n'
    paragon += f'SUMA: {suma:35.2f}\n'

    return paragon


if __name__ == "__main__":
    # Najpierw wczytujemy dane z pliku do listy rekordow.
    lista_rekordow = wczytaj_towary()
    # pprint(lista_rekordow)
    # Potem tworzymy tekst paragonu i wyswietlamy go na ekranie.
    paragon = stworz_paragon(lista_rekordow)
    print(paragon)
