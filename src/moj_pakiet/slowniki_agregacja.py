"""
Demonstracja agregacji danych w slownikach na kilka roznych sposobow.

Intencja tego modulu jest porownanie kilku wariantow rozwiazywania
tego samego problemu: zliczania wystapien elementow oraz grupowania
ich wedlug wspolnego klucza. Material jest celowo powtorzeniowy, bo
pokazuje nie jeden "jedyny sluszny" zapis, ale kilka idiomow Pythona,
ktore warto rozpoznawac i umiec porownac.

W pierwszej czesci plik pokazuje zliczanie slow:

- przez jawne sprawdzanie `if key not in dict`,
- przez `dict.get`,
- przez `collections.defaultdict`.

W drugiej czesci ten sam styl porownania zostaje zastosowany do
grupowania slow po pierwszej literze:

- wariant reczny,
- wariant z `get`,
- wariant z `setdefault`,
- wariant z `defaultdict(list)`.

Najwazniejsze mechanizmy i skladnia to:

- slowniki jako struktura agregujaca,
- metoda `split()` jako zrodlo danych tekstowych,
- `dict.get`, `dict.setdefault` i `defaultdict`,
- adnotacje typow `Mapping[str, int]` oraz `Mapping[str, list[str]]`,
- petla `for` aktualizujaca akumulator.

To dobry modul do rozmowy o czytelnosci kodu, kosztach poznawczych
roznych idiomow i wyborze stylu odpowiedniego do skali problemu.
"""

import collections
from collections.abc import Mapping

def zlicz_slowa_warunkowo(tekst: str) -> Mapping[str, int]:
    """Zlicza wystapienia slow z uzyciem jawnego sprawdzania klucza.

    Funkcja prezentuje podstawowy wariant agregacji danych w slowniku:
    dla kazdego slowa sprawdzane jest, czy klucz juz istnieje, a nastepnie
    licznik jest tworzony albo zwiekszany.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        Slownik mapujacy slowo na liczbe jego wystapien.

    See Also:
        - [dict](https://docs.python.org/3/library/stdtypes.html#dict)
    """
    d: dict[str, int] = {}

    for word in tekst.split():
        # Jezeli slowo pojawia sie pierwszy raz, rozpoczynamy licznik od 1.
        if word not in d:
            d[word] = 1
        # Przy kolejnym wystapieniu zwiekszamy juz istniejacy licznik.
        else:
            d[word] = d[word] + 1

    return d


def zlicz_slowa_z_get(tekst: str) -> Mapping[str, int]:
    """Zlicza wystapienia slow z uzyciem metody ``dict.get``.

    Ta wersja realizuje te sama logike co :func:`zlicz_slowa_warunkowo`,
    ale skraca kod dzieki pobraniu wartosci domyslnej ``0`` dla brakujacego
    klucza.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        Slownik mapujacy slowo na liczbe jego wystapien.

    See Also:
        - [dict.get](https://docs.python.org/3/library/stdtypes.html#dict.get)
    """
    d: dict[str, int] = {}

    for word in tekst.split():
        d[word] = d.get(word, 0) + 1

    return d


def zlicz_slowa_z_defaultdict(tekst: str) -> Mapping[str, int]:
    """Zlicza wystapienia slow z uzyciem ``collections.defaultdict``.

    Funkcja korzysta z ``defaultdict(int)``, dzieki czemu brakujacy klucz
    automatycznie otrzymuje wartosc ``0``. Pozwala to zapisac logike
    inkrementacji w najbardziej zwiezlej postaci.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        ``defaultdict`` mapujacy slowo na liczbe jego wystapien.

    See Also:
        - [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)
    """
    # Alternatywne warianty tworzenia ``defaultdict`` o tej samej logice:
    # def f1() -> int:
    #     return 0
    #
    # d: collections.defaultdict[str, int] = collections.defaultdict(f1)
    # d: collections.defaultdict[str, int] = collections.defaultdict(lambda: 0)
    d: collections.defaultdict[str, int] = collections.defaultdict(int)

    for word in tekst.split():
        d[word] += 1

    return d


def grupuj_po_pierwszej_literze_warunkowo(tekst: str) -> Mapping[str, list[str]]:
    """Grupuje slowa po pierwszej literze z jawna obsluga brakujacego klucza.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        Slownik, w ktorym kluczem jest pierwsza litera slowa, a wartoscia
        lista slow rozpoczynajacych sie od tej litery.
    """
    d: dict[str, list[str]] = {}

    for word in tekst.split():
        first_letter = word[0]
        if first_letter not in d:
            d[first_letter] = []
        d[first_letter].append(word)

    return d


def grupuj_po_pierwszej_literze_z_get(tekst: str) -> Mapping[str, list[str]]:
    """Grupuje slowa po pierwszej literze z uzyciem ``dict.get``.

    Funkcja pobiera istniejaca liste dla danej litery albo tworzy nowa
    liste tymczasowa, do ktorej dopisywane jest kolejne slowo.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        Slownik grupujacy slowa po pierwszej literze.
    """
    d: dict[str, list[str]] = {}

    for word in tekst.split():
        first_letter = word[0]
        lista = d.get(first_letter, [])
        lista.append(word)
        d[first_letter] = lista

    return d


def grupuj_po_pierwszej_literze_z_setdefault(tekst: str) -> Mapping[str, list[str]]:
    """Grupuje slowa po pierwszej literze z uzyciem ``dict.setdefault``.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        Slownik grupujacy slowa po pierwszej literze.

    See Also:
        - [dict.setdefault](https://docs.python.org/3/library/stdtypes.html#dict.setdefault)
    """
    d: dict[str, list[str]] = {}

    for word in tekst.split():
        first_letter = word[0]
        d.setdefault(first_letter, []).append(word)

    return d


def grupuj_po_pierwszej_literze_z_defaultdict(
    tekst: str,
) -> Mapping[str, list[str]]:
    """Grupuje slowa po pierwszej literze z uzyciem ``defaultdict(list)``.

    Args:
        tekst: Napis zawierajacy slowa rozdzielone bialymi znakami.

    Returns:
        ``defaultdict`` mapujacy pierwsza litere na liste odpowiadajacych slow.
    """
    d: collections.defaultdict[str, list[str]] = collections.defaultdict(list)

    for word in tekst.split():
        d[word[0]].append(word)

    return d


if __name__ == "__main__":
    x = "mama tata mama mama tata ja"
    {
        "mama": 3,
        "tata": 2,
        "ja": 1,
    }
    print(zlicz_slowa_warunkowo(x))
    print(zlicz_slowa_z_get(x))
    print(zlicz_slowa_z_defaultdict(x))

    x = "ala alicja alina beata bartek"
    {
        "a": ["ala", "alicja", "alina"],
        "b": ["beata", "bartek"],
    }
    print(grupuj_po_pierwszej_literze_warunkowo(x))
    print(grupuj_po_pierwszej_literze_z_get(x))
    print(grupuj_po_pierwszej_literze_z_setdefault(x))
    print(grupuj_po_pierwszej_literze_z_defaultdict(x))
