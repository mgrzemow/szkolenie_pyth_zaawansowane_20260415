"""
Demonstracja roznicy miedzy zwykla funkcja zwracajaca kolekcje
a funkcja-generator oparta o `yield`.

Plik sluzy do pokazania, ze generator nie produkuje wszystkich danych
od razu. Zamiast tego zwraca obiekt iteratora, ktory dostarcza kolejne
wartosci dopiero podczas iteracji. To pozwala zobaczyc roznice miedzy
"materializacja calego wyniku" a "produkcja leniwa".

W module zestawione sa trzy warianty:

- `f1`, ktora buduje liste i zwraca gotowy wynik,
- `f2`, ktora zwraca generator przez `yield`,
- `f3`, ktora laczy generator z `functools.lru_cache`.

To ostatnie polaczenie jest celowo pokazowe i prowokuje dyskusje.
Cache dobrze wspolpracuje z funkcjami zwracajacymi zwykle wartosci,
ale w przypadku generatora zapamietujemy sam obiekt iteratora, a nie
"zestaw przyszlych wynikow". Po zuzyciu generatora kolejne uzycie tego
samego obiektu moze byc mylace.

Najwazniejsze mechanizmy i skladnia to:

- `yield` jako sygnal, ze funkcja staje sie generatorem,
- petla `for` jako konsument iteratora,
- `functools.lru_cache` jako dekorator memoizujacy,
- wypisywanie komunikatow produkcji i konsumpcji do obserwacji momentu
  wykonania kodu.

To dobry modul do rozmowy o iteratorach, jednokrotnosci zuzycia
generatorow i roznicy miedzy obiektem generatora a lista wartosci.
"""

import functools


def f1(n):
    x = []
    for i in range(n):
        print(f"Produkuję {i}")
        x.append(i)
    return x


def f2(n):
    print('start generatora')
    for i in range(n):
        print(f"Produkuję {i}")
        yield i
    print('koniec generatora')

# cachowanie generatorów to raczej zły pomysł,
# bo drugie wywołanie zwróci już pusty generator

@functools.lru_cache(maxsize=None)
def f3(n):
    print('start generatora')
    for i in range(n):
        print(f"Produkuję {i}")
        yield i
    print('koniec generatora')


if __name__ == "__main__":
    g = f3(5)
    print(g)
    for i in g:
        print(f"Konsumuję {i}")

    g = f3(5)
    print(g)
    for i in g:
        print(f"Konsumuję {i}")
