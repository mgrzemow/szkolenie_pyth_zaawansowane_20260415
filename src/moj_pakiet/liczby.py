"""Przykłady pracy z liczbami w Pythonie dla osób znających podstawy.

Ten moduł pokazuje:

- że ``int`` ma arbitralną precyzję i działa jak praktyczny ``bigint``,
- że obliczenia na ``float`` mogą dawać błędy reprezentacji i zaokrągleń,
- że do porównań zmiennoprzecinkowych warto używać np. ``math.isclose``,
- że moduły ``fractions`` i ``decimal`` służą do dokładniejszych obliczeń
  niż zwykły ``float``.

Kod demonstracyjny jest umieszczony pod ``if __name__ == "__main__":``.
Dzięki temu po imporcie modułu przykłady nie uruchamiają się automatycznie.

## Dokumentacja Python

- [Built-in Types - Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [math.isclose](https://docs.python.org/3/library/math.html#math.isclose)
- [fractions](https://docs.python.org/3/library/fractions.html)
- [decimal](https://docs.python.org/3/library/decimal.html)
"""


if __name__ == "__main__":
    import decimal as dc
    import fractions
    import math

    # Pythonowe ``int`` ma arbitralną precyzję, więc bardzo duże liczby całkowite
    # nie przepełniają się tak jak w wielu innych językach.
    x = 999**999
    print(x)
    print(type(x))

    # Pierwiastek z liczby ujemnej zapisany przez potęgowanie daje liczbę zespoloną.
    print((-9) ** 0.5)
    print(type((-9) ** 0.5))

    # Klasyczny przykład błędu reprezentacji liczb zmiennoprzecinkowych.
    x = 0.1 + 0.2
    y = 0.3
    print(x == y)
    print(x, y)

    # Do porównań ``float`` lepiej używać przybliżonego porównania.
    print(math.isclose(x, y))

    # ``fractions.Fraction`` pozwala reprezentować ułamki zwykłe dokładnie.
    ulamek = fractions.Fraction(1, 3)
    print(ulamek)

    # ``decimal.Decimal`` pozwala liczyć dokładnie w systemie dziesiętnym.
    x = dc.Decimal("0.1") + dc.Decimal("0.2")
    y = dc.Decimal("0.3")
    print(x)
    print(x == y)
