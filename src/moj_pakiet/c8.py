"""
Demonstracja prostego dekoratora modyfikującego wartość zwracaną przez funkcję.

Plik pokazuje dekorator, który opakowuje oryginalną funkcję i próbuje
znormalizować jej wynik numeryczny do jednego z prostych typów:

- najpierw do `int`,
- jeśli to się nie uda, do `float`.

Przykład jest celowo niewielki i skupia się na samym mechanizmie dekorowania
funkcji oraz przechwytywaniu wyniku zwracanego przez funkcję bazową.
"""

import functools


# Dekorator przechwytuje wynik funkcji i próbuje przekonwertować go
# do prostszego typu liczbowego.
def to_int_float(f_oryginalna):
    # `wraps` zachowuje metadane oryginalnej funkcji, np. nazwę i docstring.
    @functools.wraps(f_oryginalna)
    def f_nowa(*args, **kwargs):
        # Najpierw uruchamiamy właściwą funkcję i pobieramy jej wynik.
        w = f_oryginalna(*args, **kwargs)
        try:
            # Pierwsza próba: zwrot jako liczba całkowita.
            return int(w)
        except ValueError:
            # Druga próba: jeśli `int` się nie uda, próbujemy `float`.
            return float(w)
        return w

    return f_nowa


# Prosta funkcja wejściowa do pokazania działania dekoratora.
@to_int_float
def f1(p):
    return p


if __name__ == "__main__":
    # Kolejne wywołania pokazują, jak dekorator zmienia typ wartości zwracanej.
    print(f1(11))
    print(f1(11.222))
    print(f1("12"))
    print(f1("12.1123"))
    # print(f1("asdasdas"))

    # Dzięki `functools.wraps` dekorowana funkcja zachowuje swoją tożsamość.
    print(f1)
    print(f1.__closure__[0].cell_contents)
