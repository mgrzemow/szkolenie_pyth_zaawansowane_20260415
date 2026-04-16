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
```

2. Po każdym towarze program dodaje dane do słownika zakupów w formacie:

```python
{
    'chleb': (3, 'szt', 4.6),
    'cebula': (1.55, 'kg', 2.5),
}
```

3. Jeżeli towar już raz wystąpił i jest w słowniku to zamiast dodawać go
   drugi raz - zwiększamy ilość.

3. Używając danych ze słownika stowrzonego w pkt 2 wypisuje na ekran paragon w formie:

```text
Pietruszka  2.0 kg x 4.60     9.20
Banany      3.0 kg x  3.5    10.50
----------------------------------
SUMA:                        19.70
```

Kolumny mają mieć szerokości:

- nazwa - 12 znaków,
- ilość - 2 znaki przed przecinkiem i 2 po
- jednostka miary - 4 znaki
- cena - 3 znaki przed przecinkiem i 2 po
- wartość pozycji - 5 znaków przed i 2 po
- SUMA - 7 znaków przed i 2 po

## Podpowiedzi:

- formatowanie f-stringow

## Rozszerzenia ćwiczenia:

- co by było gdyby mógł wystąpić towar o różnych jednostkach miary.
"""

import collections
from collections.abc import Mapping
from pathlib import Path
from pprint import pprint


KluczTowaru = tuple[str, str]
RekordTowaru = tuple[float, float]


class DaneTowaru(tuple):
    """Reprezentuje zagregowane dane pojedynczej pozycji towaru.

    Obiekt przechowuje dane w postaci krotki:

    - ``0`` - ilość,
    - ``1`` - cena.

    Klasa dziedziczy po ``tuple`` i pozostaje niemutowalna, ale udostępnia
    metodę domenową :meth:`dodaj_ilosc`, która zwraca nowy obiekt z
    uaktualnionymi danymi.

    Niejawna reguła biznesowa zastosowana w tej klasie jest następująca:

    - ilość jest sumowana z poprzednią wartością,
    - cena **nie** jest uśredniana ani sumowana,
    - cena po agregacji jest przejmowana z najnowszego rekordu wejściowego.

    To oznacza, że jeśli ten sam towar i jednostka miary pojawią się kilka razy,
    końcowa ilość będzie sumą wszystkich wpisów, a końcowa cena będzie równa
    cenie z ostatnio przetworzonego rekordu.

    Dokumentacja Python:

    - [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
    """

    idx_ilosc: int = 0

    def dodaj_ilosc(self, dane: RekordTowaru) -> "DaneTowaru":
        """Zwraca nowy obiekt z dodaną ilością i zaktualizowaną ceną.

        Metoda służy do agregowania kolejnych rekordów tego samego towaru.
        Jeżeli obiekt jest pusty, traktowany jest jako brak wcześniejszych danych
        i zwracana jest nowa instancja z przekazanym rekordem.

        Jeśli obiekt zawiera już dane, stosowane są następujące reguły:

        - ilość z bieżącego obiektu i nowego rekordu jest sumowana,
        - pozostałe pola są pobierane z nowego rekordu,
        - w obecnym modelu oznacza to przejęcie najnowszej ceny.

        Args:
            dane: Krotka ``(ilosc, cena)`` reprezentująca nowy rekord tego
                samego towaru i tej samej jednostki miary.

        Returns:
            Nowa instancja ``DaneTowaru`` z uaktualnioną ilością i ceną.
        """
        if len(self) == 0:
            return DaneTowaru(dane)
        return DaneTowaru((self[self.__class__.idx_ilosc] + dane[0], *dane[1:]))


RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "towary.txt"
SlownikTowarow = collections.defaultdict[KluczTowaru, DaneTowaru]
WidokTowarow = Mapping[KluczTowaru, DaneTowaru]


def wczytaj_towary(
    plik_towary: Path = RESOURCE_FILE,
) -> SlownikTowarow:
    """Wczytuje towary z pliku i agreguje je w słowniku.

    Funkcja odczytuje dane z pliku tekstowego i buduje słownik, w którym:

    - kluczem jest para ``(nazwa_towaru, jednostka_miary)``,
    - wartością jest ``DaneTowaru`` przechowujące ``(ilosc, cena)``.

    Przy ponownym wystąpieniu tego samego klucza funkcja nie nadpisuje danych
    wprost, tylko wywołuje metodę :meth:`DaneTowaru.dodaj_ilosc`.

    Niejawne reguły biznesowe tego etapu:

    - rekordy są grupowane po ``(towar, jednostka_miary)``,
    - ilości są sumowane,
    - cena końcowa pochodzi z ostatniego przetworzonego rekordu dla danego klucza.

    Args:
        plik_towary: Ścieżka do pliku z danymi o towarach.

    Returns:
        ``defaultdict`` mapujący ``(towar, jm)`` na ``DaneTowaru``.

    Raises:
        FileNotFoundError: Gdy plik wejściowy nie istnieje.
        ValueError: Gdy wartości liczbowe w pliku mają niepoprawny format.

    See Also:
        - [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)
    """
    slownik_rekordow: SlownikTowarow = collections.defaultdict(DaneTowaru)

    with plik_towary.open("rt", encoding="utf8") as f:
        for linia in f:
            # Pomijamy puste linie i komentarze, aby przetwarzać tylko dane wejściowe.
            if linia.strip() and not linia.strip().startswith("#"):
                towar, ilosc, jm, cena, *_ = linia.split()
                ilosc_float = float(ilosc.strip("'"))
                cena_float = float(cena.strip("'"))
                slownik_rekordow[(towar, jm)] = slownik_rekordow[(towar, jm)].dodaj_ilosc(
                    (ilosc_float, cena_float)
                )

    return slownik_rekordow


def stworz_paragon(slownik_rekordow: WidokTowarow) -> str:
    """Buduje tekstową reprezentację paragonu na podstawie słownika rekordów.

    Funkcja iteruje po wcześniej zagregowanych danych i tworzy wielowierszowy
    napis gotowy do wypisania na ekran.

    Args:
        slownik_rekordow: Mapowanie, w którym kluczem jest para
            ``(nazwa_towaru, jednostka_miary)``, a wartością obiekt
            ``DaneTowaru`` przechowujący ``(ilosc, cena)``.

    Returns:
        Napis reprezentujący paragon wraz z linią sumy końcowej.
    """
    paragon = ""
    suma = 0.0

    for (towar, jm), (ilosc, cena) in slownik_rekordow.items():
        # Dla każdej pozycji obliczamy wartość i aktualizujemy sumę końcową.
        wartosc = round(ilosc * cena, 2)
        suma = round(suma + wartosc, 2)
        paragon += f"{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n"

    paragon += "-" * 41 + "\n"
    paragon += f"SUMA: {suma:35.2f}\n"

    return paragon


if __name__ == "__main__":
    slownik_rekordow = wczytaj_towary()
    pprint(slownik_rekordow)
    paragon = stworz_paragon(slownik_rekordow)
    print(paragon)
