"""
przerobić funkcje wczytaj_towary na gneratory z yield
sparametryzować:
- upper / lower
- znak '#' do filtrowania
- znak ' do pol z liczbami
"""

from pathlib import Path
from pprint import pprint
from typing import Iterable, Iterator


RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "towary.txt"

def standaryzacja_linii(g_linii: Iterable[str], upper: bool = False) -> Iterator[str]:
    for linia in g_linii:
        linia = linia.strip()
        if upper:
            linia = linia.upper()
        else:
            linia = linia.lower()
        yield linia

def filtrowanie_linii(g_linii: Iterable[str], znak_komentarz: str = '#') -> Iterator[str]:
    for linia in g_linii:
        if linia and not linia.startswith(znak_komentarz):
            yield linia

def konwersja_do_rekordu(g_linii: Iterable[str], znak_liczby: str = "'") -> Iterator[tuple[str, float, str, float]]:
    for linia in g_linii:
        towar, ilosc, jm, cena, *_ = linia.split()
        ilosc_float = float(ilosc.strip(znak_liczby))
        cena_float = float(cena.strip(znak_liczby))
        yield (towar, ilosc_float, jm, cena_float)

def wczytaj_towary(
    plik_towary: Path = RESOURCE_FILE,
) -> list[tuple[str, float, str, float]]:

    with plik_towary.open("rt", encoding="utf8") as f:
        # zamieniam na małe i czyszczę białe znaki
        g1 = standaryzacja_linii(f)
        # filtruję tylko linie zawierające znak '@' i pomijam puste oraz komentarze
        g2 = filtrowanie_linii(g1)
        # konwertuję dane na odpowiednie typy i tworzę krotki
        g3 = konwersja_do_rekordu(g2)
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
