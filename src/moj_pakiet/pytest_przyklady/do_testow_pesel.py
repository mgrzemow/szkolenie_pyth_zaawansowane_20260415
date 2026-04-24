"""
Prosty moduł do demonstracji podstaw pytesta.

Funkcja `rob_pesel` jest celowo mała i deterministyczna, dzięki czemu nadaje
się do pokazania:
- zwykłych asercji,
- parametryzacji,
- fixture z danymi testowymi.
"""


def _sprawdz_argumenty(rok, miesiac, dzien, nr, plec_facet):
    """Waliduje podstawowe argumenty wejściowe uproszczonego generatora PESEL."""
    if type(rok) is not int:
        raise TypeError("rok musi być liczbą całkowitą")
    if type(miesiac) is not int:
        raise TypeError("miesiac musi być liczbą całkowitą")
    if type(dzien) is not int:
        raise TypeError("dzien musi być liczbą całkowitą")
    if type(nr) is not int:
        raise TypeError("nr musi być liczbą całkowitą")
    if type(plec_facet) is not bool:
        raise TypeError("plec_facet musi być wartością bool")

    if not 1 <= miesiac <= 12:
        raise ValueError("miesiac musi być z zakresu 1..12")
    if not 1 <= dzien <= 31:
        raise ValueError("dzien musi być z zakresu 1..31")
    if not 0 <= nr <= 999:
        raise ValueError("nr musi być z zakresu 0..999")


def rob_pesel(rok, miesiac, dzien, nr, plec_facet):
    """Buduje uproszczony numer PESEL na podstawie przekazanych danych."""
    _sprawdz_argumenty(rok, miesiac, dzien, nr, plec_facet)

    # Dla osób urodzonych od 2000 roku miesiąc jest zapisany z przesunięciem o 20.
    miesiac_w_peselu = miesiac + 20 if rok >= 2000 else miesiac

    # Najpierw składamy bazę bez cyfry kontrolnej.
    baza = (
        f"{str(rok)[-2:]}"
        f"{miesiac_w_peselu:02d}"
        f"{dzien:02d}"
        f"{nr:03d}"
        f"{int(plec_facet)}"
    )

    # W tej wersji ćwiczeniowej cyfra kontrolna to ostatnia cyfra sumy cyfr.
    cyfra_kontrolna = str(sum(int(znak) for znak in baza))[-1]
    return baza + cyfra_kontrolna


if __name__ == "__main__":
    # Krótki przykład ręcznego uruchomienia modułu poza pytestem.
    print(rob_pesel(2002, 11, 3, 34, True))
