"""
# Ćwiczenie:

1. Wczytać z konsoli długości 3 boków trójkąta
2. Sprawdzić i wypisać na ekran:
   - czy trójkąt da się stworzyć
   - czy jest prostokątny
   - czy jest równoramienny
   - czy jest równoboczny

## Podpowiedzi:

- czy niektóre warunki zależą od siebie i w jaki sposób? Jak to wpłynie na zagnieżdżenie if-ów?

## Rozszerzenia ćwiczenia:

- czy da się wpisać takie dane, żeby wyszedł trójkąt równoramienny i prostokątny? Dlaczego nie i jak to ominąć?
- co robi eval()?
"""

import math


def analizuj_trojkat(a: float, b: float, c: float) -> tuple[bool, bool, bool, bool]:
    """Analizuje podstawowe wlasciwosci trojkata na podstawie dlugosci bokow.

    Funkcja sprawdza, czy z podanych trzech bokow da sie zbudowac trojkat,
    a jesli tak, wyznacza trzy dodatkowe cechy:

    - czy trojkat jest prostokatny,
    - czy trojkat jest rownoramienny,
    - czy trojkat jest rownoboczny.

    Logika obliczen pozostaje zgodna z wersja proceduralna z cwiczenia:

    - warunek istnienia trojkata opiera sie na nierownosciach trojkata,
    - trojkat prostokatny jest wykrywany przez porownanie sum kwadratow bokow,
    - trojkat rownoramienny ma co najmniej dwa rowne boki,
    - trojkat rownoboczny ma trzy rowne boki.

    Args:
        a: Dlugosc pierwszego boku trojkata.
        b: Dlugosc drugiego boku trojkata.
        c: Dlugosc trzeciego boku trojkata.

    Returns:
        Krotke czterech wartosci logicznych w kolejnosci:

        - ``istnieje`` - czy trojkat da sie zbudowac,
        - ``prostokatny`` - czy trojkat jest prostokatny,
        - ``rownoramienny`` - czy trojkat jest rownoramienny,
        - ``rownoboczny`` - czy trojkat jest rownoboczny.

        Dla danych, z ktorych nie da sie zbudowac trojkata, pozostale trzy
        wartosci sa zwracane jako ``False``.
    """
    # Najpierw sprawdzamy podstawowy warunek istnienia trojkata.
    istnieje = a + b > c and a + c > b and b + c > a

    if not istnieje:
        return False, False, False, False

    # Dodatkowe wlasciwosci analizujemy tylko dla poprawnego trojkata.
    prostokatny = (
        math.isclose(a ** 2 + b ** 2, c ** 2)
        or math.isclose(a ** 2 + c ** 2, b ** 2)
        or math.isclose(b ** 2 + c ** 2, a ** 2)
    )
    rownoramienny = a == b or a == c or b == c
    rownoboczny = a == b == c

    return istnieje, prostokatny, rownoramienny, rownoboczny


if __name__ == '__main__':
    a = eval(input('Podaj długość boku: '))
    b = eval(input('Podaj długość boku: '))
    c = eval(input('Podaj długość boku: '))

    # Analiza trojkata jest wydzielona do osobnej funkcji.
    istnieje, prostokatny, rownoramienny, rownoboczny = analizuj_trojkat(a, b, c)

    if not istnieje:
        print('Takiego trójkąta nie da się zbudować.')
    else:
        print('Trójkąt da się zbudować.')
        print('Trójkąt jest prostokątny.' if prostokatny else 'Trójkąt nie jest prostokątny.')
        print('Trójkąt jest równoramienny.' if rownoramienny else 'Trójkąt nie jest równoramienny.')
        print('Trójkąt jest równoboczny.' if rownoboczny else 'Trójkąt nie jest równoboczny.')
        print('----------------------')
