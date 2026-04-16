"""Podstawy słowników w Pythonie.

Słownik ``dict`` jest strukturą danych przechowującą pary:

- klucz -> wartość

Najważniejsze cechy słowników:

- klucze muszą być hashowalne, czyli zwykle niemutowalne,
- wartości mogą być dowolnymi obiektami,
- dostęp do wartości odbywa się przez klucz,
- słownik dobrze nadaje się do szybkiego wyszukiwania danych po nazwie,
- od współczesnych wersji Pythona słownik zachowuje kolejność dodawania wpisów.

Typowe zastosowania słownika:

- mapowanie nazw na wartości,
- konfiguracja,
- prosty rekord danych,
- grupowanie i agregacja informacji.

Najczęstsze operacje na słownikach to:

- tworzenie pustego i wypełnionego słownika,
- odczyt po kluczu,
- dodawanie lub nadpisywanie wartości,
- sprawdzanie obecności klucza,
- iterowanie po kluczach, wartościach lub parach ``(klucz, wartość)``,
- sortowanie po kluczach lub wartościach.

## Dokumentacja Python

- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
- [Dictionary view objects](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects)
"""


if __name__ == "__main__":
    # Pusty słownik można utworzyć na dwa podstawowe sposoby.
    d = {}
    print(d)
    d = dict()
    print(d)

    # Słownik z danymi początkowymi.
    d = {"a": 1, "b": 2, "c": 3}
    print(d)

    # Operator ``in`` dla słownika sprawdza obecność klucza, a nie wartości.
    print(1 in d)
    print("a" in d)

    # Odczyt wartości po kluczu.
    print(d["a"])

    # Iterowanie po samych kluczach.
    for klucz in d:
        print(klucz, d[klucz])

    # Można też iterować jawnie po parach ``(klucz, wartość)``.
    for klucz, wartosc in d.items():
        print(klucz, wartosc)

    # Dodawanie nowych wpisów i nadpisywanie istniejących.
    d["e"] = 5
    d["d"] = 4
    d["a"] = 111
    print(d)

    # Odczyt wszystkich kluczy, wartości i par.
    print(list(d.keys()))
    print(list(d.values()))
    print(list(d.items()))

    # Sortowanie kluczy zwraca listę kluczy.
    print(sorted(d))

    # Sortowanie po kluczach i złożenie z powrotem do słownika.
    print(dict(sorted(d.items())))

    # Sortowanie po wartościach.
    print(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))

    # Łączenie słowników przez rozpakowanie ``**``.
    d1 = {"f": 66, **d}
    print(d1)

    # Słownik może też służyć jako prosty rekord danych.
    d = {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 30,
    }
    print(d["imie"])

    # Kolejność pól w słowniku nie musi odpowiadać kolejności znaczeniowej danych.
    d = {
        "nazwisko": "Kowalski",
        "wiek": 30,
        "imie": "Jan",
        "inne_pole": "wartosc",
    }
    print(d["imie"])

