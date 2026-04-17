"""
przerobić funkcje wczytaj_towary na wyrażenia generatorowe
"""

from pathlib import Path
from pprint import pprint


RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "towary.txt"


def wczytaj_towary(
    plik_towary: Path = RESOURCE_FILE,
) -> list[tuple[str, float, str, float]]:

    with plik_towary.open("rt", encoding="utf8") as f:
        # zamieniam na małe i czyszczę białe znaki
        g1 = (linia.lower().strip() for linia in f)
        # filtruję tylko linie zawierające znak '@' i pomijam puste oraz komentarze
        g2 = (linia.split() for linia in g1 if linia and not linia.startswith("#"))
        # konwertuję dane na odpowiednie typy i tworzę krotki
        g3 = (
            (towar, float(ilosc.strip("'")), jm, float(cena.strip("'")))
            for towar, ilosc, jm, cena, *_ in g2
        )

        return list(g3)


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
    paragon = ""
    suma = 0.0

    for towar, ilosc, jm, cena in lista_rekordow:
        # Dla kazdej pozycji obliczamy wartosc czastkowa i aktualizujemy sume.
        wartosc = round(ilosc * cena, 2)
        suma = round(suma + wartosc, 2)
        paragon += f"{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n"

    paragon += "-" * 41 + "\n"
    paragon += f"SUMA: {suma:35.2f}\n"

    return paragon


if __name__ == "__main__":
    # Najpierw wczytujemy dane z pliku do listy rekordow.
    lista_rekordow = wczytaj_towary()
    # pprint(lista_rekordow)
    # Potem tworzymy tekst paragonu i wyswietlamy go na ekranie.
    paragon = stworz_paragon(lista_rekordow)
    print(paragon)
