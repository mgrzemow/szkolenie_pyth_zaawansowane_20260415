"""Podstawy zbiorów w Pythonie.

Zbiór ``set`` jest nieuporządkowaną kolekcją unikalnych elementów.

Najważniejsze cechy zbiorów:

- nie przechowują duplikatów,
- służą głównie do szybkiego sprawdzania przynależności i operacji na zbiorach,
- mogą zawierać tylko elementy hashowalne,
- nie zachowują znaczącej kolejności elementów.

Typowe zastosowania zbiorów:

- usuwanie duplikatów,
- sprawdzanie, czy element należy do kolekcji,
- obliczanie części wspólnej, sumy, różnicy i różnicy symetrycznej,
- praca na obiektach, które reprezentują unikalne wartości.

Warto pamiętać, że hashowalność zwykle oznacza niemutowalność z punktu widzenia
tożsamości obiektu. Jeżeli obiekt umieszczony w zbiorze zmienia stan wpływający
na ``__hash__`` albo ``__eq__``, może to prowadzić do trudnych błędów.

## Dokumentacja Python

- [set](https://docs.python.org/3/library/stdtypes.html#set)
- [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset)
- [hash](https://docs.python.org/3/library/functions.html#hash)
"""


if __name__ == "__main__":
    import dataclasses
    from typing import Any

    # Pusty zbiór tworzymy przez ``set()``, a nie przez ``{}``,
    # bo ``{}`` oznacza pusty słownik.
    s = set()
    print(type(s))

    # Zbiór z wartościami początkowymi.
    s = {1, 2, 3}
    print(s)

    # Zbiory nie przechowują duplikatów.
    s.add(3)
    print(s)

    # ``3`` i ``3.0`` są równe, więc w zbiorze traktowane są jak ten sam element.
    s.add(3.0)
    print(s)
    print(3 == 3.0)

    # Do zbioru można dodać np. krotkę, bo jest hashowalna.
    s.add((5, 6, 7))
    print(s)

    # Iterowanie po zbiorze.
    for e in s:
        print(e)

    # Podstawowe operacje na zbiorze.
    print(len(s))
    print(2 in s)
    s.remove(2)
    print(s)
    s.discard(999)  # ``discard`` nie zgłasza błędu, jeśli elementu nie ma.
    print(s)

    x = ["ala", "ma", "kota", "ala", "ma", "kota"]

    # Najprostsze usuwanie duplikatów przez konwersję do zbioru.
    print(list(set(x)))

    # A jak zrobić to bez zmiany kolejności?
    print(list({e: None for e in x}.keys()))

    s = set(x)
    print("ala" in s)
    for e in s:
        print(e)

    # Klasyczne operacje teoriomnogościowe.
    abcdef = set("abcdef")
    defghi = set("defghi")
    print(defghi & abcdef)  # część wspólna
    print(defghi | abcdef)  # suma zbiorów
    print(defghi - abcdef)  # różnica
    print(defghi ^ abcdef)  # różnica symetryczna

    # Haszowalność.
    print(hash("ala"))
    print("mama".__hash__())
    print(hash("mama"))

    # Lista nie jest hashowalna, więc nie można dodać jej do zbioru.
    #
    # s = set()
    # x = [1, 2, 3]
    # s.add(x)

    class ParaHashowalna:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __hash__(self):
            # Najprostszy sposób wyliczenia hasza z atrybutów definiujących tożsamość.
            return hash((self.x, self.y))

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

    # Taki obiekt można dodać do zbioru, ale jego mutowanie jest niebezpieczne.
    a1 = ParaHashowalna("mama", 11)
    a2 = ParaHashowalna("tata", 22)
    s = set()
    s.add(a1)
    s.add(a1)
    s.add(a2)
    print(s)

    # Zmiana pola wpływającego na hasz obiektu po włożeniu do zbioru to zły pomysł.
    a1.x = "tata"
    for e in s:
        print(e.x)

    @dataclasses.dataclass(frozen=True)
    class RekordFrozen:
        x: str

    # ``dataclass(frozen=True)`` daje prosty sposób budowy niezmiennego,
    # hashowalnego obiektu.
    a1 = RekordFrozen("mama")
    a2 = RekordFrozen("tata")
    s = set()
    s.add(a1)
    s.add(a1)
    s.add(a2)
    print(s)
    for e in s:
        print(e.x)

    class RekordRecznieMrozony:
        def __init__(self, x):
            self.x = x
            self._frozen = True

        def __hash__(self):
            return hash(self.x)

        def __eq__(self, other):
            return self.x == other.x

        def __setattr__(self, name: str, value: Any) -> None:
            if hasattr(self, "_frozen") and self._frozen:
                raise AttributeError("Obiekt jest zamrożony, nie można zmienić atrybutów.")
            super().__setattr__(name, value)

    # Ręczne blokowanie zmian atrybutów daje podobny efekt dydaktyczny.
    a1 = RekordRecznieMrozony("mama")
    a2 = RekordRecznieMrozony("tata")
    s = set()
    s.add(a1)
    s.add(a1)
    s.add(a2)
    print(s)

    try:
        a1.x = "tata"
    except AttributeError as e:
        print(e)

    for e in s:
        print(e.x)
