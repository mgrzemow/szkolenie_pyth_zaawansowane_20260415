"""Podstawy list, krotek i unpackingu w Pythonie.

Ten moduł zakłada znajomość podstaw języka i porządkuje kilka ważnych pojęć
związanych z sekwencjami.

## Listy

Lista:

- jest uporządkowaną kolekcją elementów,
- jest mutowalna, czyli można ją zmieniać po utworzeniu,
- może przechowywać elementy różnych typów,
- dobrze nadaje się do przechowywania danych, które będą dopisywane,
  usuwane albo modyfikowane.

Najczęstsze operacje na listach to:

- odczyt elementu po indeksie,
- wycinanie fragmentów przez slicing,
- dopisywanie przez ``append`` i ``extend``,
- usuwanie przez ``pop`` albo ``remove``,
- sprawdzanie długości przez ``len``.

## Krotki

Krotka:

- również jest uporządkowaną kolekcją elementów,
- jest niemutowalna, czyli nie można podmieniać jej elementów po utworzeniu,
- często nadaje się do reprezentowania stałego rekordu danych,
- bywa trochę lżejsza i semantycznie lepiej komunikuje, że układ danych
  nie powinien się zmieniać.

Warto pamiętać, że niemutowalność krotki dotyczy samej struktury krotki.
Jeżeli wewnątrz krotki znajdują się obiekty mutowalne, np. listy,
to ich zawartość nadal można zmieniać.

## Unpacking

Unpacking to rozpakowywanie elementów sekwencji do wielu zmiennych naraz.
Można go używać zarówno dla list, jak i dla krotek, o ile liczba elementów
zgadza się z liczbą zmiennych albo użyjemy operatora ``*`` do zebrania reszty.

Przykłady zastosowań unpackingu:

- przypisanie wielu wartości jednocześnie,
- rozbijanie rekordów danych na pola,
- pomijanie niepotrzebnych wartości przez ``_``,
- przechwytywanie reszty elementów przez ``*reszta``.
"""


if __name__ == "__main__":
    import collections
    import time

    # Pusta lista.
    x = []
    print(type(x))

    # Lista może przechowywać elementy różnych typów.
    x = [
        1,
        2.44,
        "mama",
        True,
    ]
    print(x)

    # Podstawowy przykład listy i rekordu zapisanego jako lista.
    lista_imion = ["ala", "ola", "ula"]
    rekord_danych = ["ola", 34, "Warszawa", 1.98]

    # Podstawowe operacje na liście: długość, indeksowanie i slicing.
    print(len(lista_imion))
    print(lista_imion[0])
    print(lista_imion[-1])
    print(lista_imion[0:2])

    # Dopisywanie pojedynczego elementu i wielu elementów.
    lista_imion.append("tomek")
    lista_imion.extend(["jan", "paweł"])
    print(lista_imion)

    # Konkatenacja list przez operator ``+=``.
    lista_imion += ["ewa", "grześ"]
    print(lista_imion)

    # Podstawowe operacje usuwania elementów.
    print(lista_imion.pop())
    print(lista_imion)
    lista_imion.remove("ola")
    print(lista_imion)

    # Sprawdzenie obecności elementu.
    print("ala" in lista_imion)

    # Uwaga na wstawianie na początek lub w środek sekwencji.
    # W praktyce, gdy chcemy często dodawać na początek, warto rozważyć ``deque``.
    for n in [50_000, 100_000, 200_000]:
        x = collections.deque()
        t1 = time.perf_counter()
        for i in range(n):
            x.insert(0, i)
        print(f"{n}: {time.perf_counter() - t1:.2f}")

    # Podstawowy unpacking.
    rekord_danych = ["ola", 34, "Warszawa", 1.98]
    imie = rekord_danych[0]
    wiek = rekord_danych[1]
    miasto = rekord_danych[2]
    wzrost = rekord_danych[3]
    print(imie, wiek, miasto, wzrost)

    # To samo można zapisać krócej przez unpacking.
    imie, wiek, miasto, wzrost = rekord_danych
    print(imie, wiek, miasto, wzrost)

    # Gdy liczba elementów może być zmienna, można zebrać nadmiarowe dane przez ``*``.
    rekord_danych_2 = ["ola", 34, "Warszawa", 1.98, "Polska"]
    rekord_danych_3 = ["ola", 34, "Warszawa", 1.98, "Polska", "Europa"]
    lista_rekordow = [
        rekord_danych,
        rekord_danych_2,
        rekord_danych_3,
    ]
    print(lista_rekordow)

    for r in lista_rekordow:
        imie, wiek, miasto, wzrost, *reszta = r
        print(imie, wiek, miasto, wzrost, reszta)

    # Unpacking można też wykonać bezpośrednio w nagłówku pętli.
    for imie, wiek, miasto, wzrost, *reszta in lista_rekordow:
        print(imie, wiek, miasto, wzrost, reszta)

    # Konwencyjnie ``_`` oznacza, że wartość nas nie interesuje.
    for imie, _, miasto, _, *_ in lista_rekordow:
        print(imie, miasto)

    # Możliwe jest też zagnieżdżone rozpakowanie.
    r = ["Jan", "Nowak", ["Kraków", "Długa", 51]]
    imie, nazwisko, (miasto, ulica, nr) = r
    print(imie, nazwisko, miasto, ulica, nr)

    # Unpacking działa zarówno dla list, jak i dla krotek.
    a, b, c = (1, 2, 3)
    print(a, b, c)

    # Krotki są niemutowalne i często służą jako prosty, stały rekord danych.
    x = (1, 2, 3)
    print(type(x))
    print(len(x))
    print(x[0])
    print(x[1:])

    # Jednoelementowa krotka wymaga przecinka.
    x = (9,)
    print(x)

    # Tam, gdzie jest to jednoznaczne, nawiasy można pominąć.
    k = 1, 2, 3
    print(k, type(k))

    # Krotkę można też łączyć z inną krotką.
    print((1, 2) + (3, 4))

    # Uwaga: cała krotka jest niemutowalna, ale jej elementy nie muszą takie być.
    # To zły zwyczaj dydaktyczny, bo łatwo wprowadza w błąd.
    k = ([], [])
    k[0].append(1)
    k[0].append(2)
    k[0].append(3)
    print(k)
