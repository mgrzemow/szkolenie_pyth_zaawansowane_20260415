"""Podstawy wartości logicznych i warunków w Pythonie.

Ten moduł porządkuje kilka ważnych pojęć związanych z logiką w Pythonie:

- typ ``bool`` ma tylko dwie wartości: ``True`` i ``False``,
- ``bool`` jest szczególnym podtypem ``int``, dlatego
  ``True == 1`` oraz ``False == 0``,
- w warunkach Python interpretuje obiekty w *kontekście logicznym*,
  a nie tylko jako jawne wartości typu ``bool``,
- operatory ``and``, ``or`` i ``not`` działają z mechanizmem short-circuit,
  czyli kończą obliczenia wcześniej, jeśli wynik jest już znany,
- obiekty mogą same definiować swoje zachowanie logiczne przez metodę
  ``__bool__`` albo pośrednio przez ``__len__``.

W praktyce w kontekście logicznym za fałszywe najczęściej uznawane są:

- ``False``,
- ``None``,
- ``0`` i ``0.0``,
- puste napisy, listy, krotki, zbiory i słowniki.

Za prawdziwe uznawana jest większość pozostałych obiektów.

Operatory logiczne w Pythonie nie zawsze zwracają ``True`` albo ``False``.
``and`` i ``or`` często zwracają jeden z operandów, co bywa bardzo użyteczne,
ale wymaga ostrożności przy czytaniu kodu.

## Dokumentacja Python

- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [bool](https://docs.python.org/3/library/functions.html#bool)
"""


if __name__ == "__main__":
    import re

    # ``bool`` jest podtypem ``int``.
    print(True == 1)
    print(False == 0)
    print(type(True))

    # Podstawowe operacje logiczne.
    print(True and False)
    print(True or False)
    print(not True)

    # W Pythonie wiele różnych obiektów ma określone zachowanie w kontekście logicznym.
    print(bool(0))
    print(bool(1))
    print(bool(""))
    print(bool("tekst"))
    print(bool([]))
    print(bool([1, 2, 3]))
    print(bool(None))

    # Wynik ``re.match`` to albo obiekt dopasowania, albo ``None``.
    x = re.match(r"\d\d", "8d")
    print(x)
    print(bool(x))

    class A:
        # To niebezpieczne: biblioteka sprawdzająca ``if x:`` może potraktować
        # taki obiekt jak wartość fałszywą, choć to nie jest ``None``.
        def __bool__(self):
            print("wywołanie __bool__")
            return False

    x = A()

    # Wartość logiczna obiektu może wynikać z własnej implementacji ``__bool__``.
    if x:
        print(True, x)
    else:
        print(False, x)

    # ``and`` stosuje short-circuiting: jeśli pierwszy operand jest fałszywy,
    # drugi nie jest już sprawdzany.
    x = ""
    if x and x[0] == "a":
        print(True, x)
    else:
        print(False, x)

    # ``and`` i ``or`` zwracają operand, a niekoniecznie typ ``bool``.
    print(None and 55)
    print(None or 55)
    print("" or "domyślna wartość")
