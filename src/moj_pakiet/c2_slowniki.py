"""Budowanie paragonu na podstawie danych zapisanych w slowniku.

Modul realizuje wersje cwiczenia, w ktorej rekordy z pliku tekstowego sa
agregowane do slownika zakupow. Kazdy wpis w pliku opisuje pojedyncza pozycje
w formacie:

```text
Banany 2.4 kg 3.5
Kiwi 3 szt 2.3
Piwo 4 szt 2.4
Kiwi 3 szt 2.3
```

Po wczytaniu danych powstaje slownik, w ktorym:

- kluczem jest para ``(nazwa_towaru, jednostka_miary)``,
- wartoscia jest para ``(ilosc, cena_jednostkowa)``.

Takie podejscie rozwiazuje typowy problem ze slownikami w tym zadaniu:
ten sam towar moze pojawic sie wielokrotnie, a jego ilosc nalezy wtedy
zsumowac zamiast dopisywac kolejny rekord. W efekcie modul pozwala:

1. wczytac i zagregowac dane z pliku,
2. przygotowac tekstowa reprezentacje paragonu,
3. zachowac czytelny podzial na logike wczytywania i logike formatowania.

Paragon jest zwracany jako zwykly napis gotowy do wypisania w terminalu.
Kazda linia zawiera nazwe towaru, ilosc, jednostke miary, cene jednostkowa
i wartosc pozycji. Ostatnia linia zawiera sume wszystkich pozycji.
"""

from pathlib import Path


#: Domyslna sciezka do pliku z danymi o towarach.
RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "towary.txt"


def wczytaj_towary(
    plik_towary: Path = RESOURCE_FILE,
) -> dict[tuple[str, str], tuple[float, float]]:
    """Wczytuje towary z pliku i agreguje je w slowniku zakupow.

    Funkcja przetwarza plik tekstowy linia po linii. Kazda niepusta linia,
    ktora nie zaczyna sie od ``#``, jest interpretowana jako rekord w formacie
    ``nazwa ilosc jednostka cena``.

    Kluczem slownika wynikowego jest para ``(nazwa_towaru, jednostka_miary)``.
    Dzieki temu ten sam towar moze wystepowac w roznych jednostkach miary
    bez ryzyka nadpisania danych. Jezeli w pliku kilka razy pojawi sie ta sama
    para ``(nazwa, jednostka)``, ilosc zostanie zsumowana.

    Args:
        plik_towary: Sciezka do pliku z danymi wejsciowymi. Domyslnie jest to
            plik ``resources/towary.txt`` znajdujacy sie w katalogu projektu.

    Returns:
        Slownik, w ktorym:

        - klucz ma postac ``(nazwa_towaru, jednostka_miary)``,
        - wartosc ma postac ``(ilosc, cena_jednostkowa)``.

    Raises:
        FileNotFoundError: Gdy wskazany plik nie istnieje.
        ValueError: Gdy liczba lub uklad pol w wierszu nie odpowiadaja
            oczekiwanemu formatowi.

    Examples:
        Dla danych:

        ```text
        Kiwi 3 szt 2.3
        Kiwi 2 szt 2.3
        Banany 1.5 kg 4.5
        ```

        wynik bedzie mial postac:

        ```python
        {
            ("Kiwi", "szt"): (5.0, 2.3),
            ("Banany", "kg"): (1.5, 4.5),
        }
        ```
    """
    slownik_rekordow = {}
    with plik_towary.open("rt", encoding="utf8") as f:
        for linia in f:
            if linia.strip() and not linia.strip().startswith("#"):
                towar, ilosc, jm, cena, *_ = linia.split()
                ilosc, cena = float(ilosc.strip("'")), float(cena.strip("'"))
                if (towar, jm) in slownik_rekordow:
                    ilosc += slownik_rekordow[(towar, jm)][0]
                slownik_rekordow[(towar, jm)] = (ilosc, cena)
    return slownik_rekordow


def stworz_paragon(slownik_rekordow: dict[tuple[str, str], tuple[float, float]]) -> str:
    """Buduje tekstowa reprezentacje paragonu na podstawie slownika zakupow.

    Funkcja przyjmuje dane w formacie zwracanym przez :func:`wczytaj_towary`
    i generuje wielowierszowy napis. Kazda pozycja paragonu zawiera:

    - nazwe towaru,
    - ilosc,
    - jednostke miary,
    - cene jednostkowa,
    - wartosc pozycji.

    Na koncu dodawana jest linia oddzielajaca oraz podsumowanie wszystkich
    pozycji. Kolejnosc pozycji odpowiada kolejnosci elementow w przekazanym
    slowniku.

    Args:
        slownik_rekordow: Slownik zakupow, w ktorym klucz ma postac
            ``(nazwa_towaru, jednostka_miary)``, a wartosc
            ``(ilosc, cena_jednostkowa)``.

    Returns:
        Sformatowany napis reprezentujacy paragon. Napis konczy sie znakiem
        nowej linii, dzieki czemu mozna go bezposrednio przekazac do ``print``.

    Examples:
        ```python
        dane = {
            ("Banany", "kg"): (2.4, 3.5),
            ("Kiwi", "szt"): (3.0, 2.3),
        }
        print(stworz_paragon(dane))
        ```
    """
    paragon = ""
    suma = 0
    for (towar, jm), (ilosc, cena) in slownik_rekordow.items():
        wartosc = round(ilosc * cena, 2)
        suma = round(suma + wartosc, 2)
        paragon += f"{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n"
    paragon += "-" * 41 + "\n"
    paragon += f"SUMA: {suma:35.2f}\n"
    return paragon


if __name__ == "__main__":
    slownik_rekordow = wczytaj_towary()
    paragon = stworz_paragon(slownik_rekordow)
    print(paragon)
