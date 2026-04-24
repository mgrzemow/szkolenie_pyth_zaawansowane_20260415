"""
Demonstracja najprostszego dekoratora funkcyjnego bez parametrow.

Celem pliku jest pokazanie podstawowej idei dekorowania funkcji:
zamiast zmieniac kod funkcji oryginalnej, owijamy ja inna funkcja,
ktora wykonuje dodatkowa logike przed i po wywolaniu oryginalu.

W tym wariancie dekorator sam jest funkcja przyjmujaca funkcje jako
argument. Zwraca nowa funkcje `f_nowa`, ktora:

- odbiera dowolne argumenty przez `*args` i `**kwargs`,
- wywoluje funkcje oryginalna,
- wypisuje komunikaty diagnostyczne,
- zwraca wynik dalej bez zmiany semantyki wywolania.

Modul wykorzystuje `functools.wraps`, czyli standardowy pomocnik
zachowujacy metadane dekorowanej funkcji, takie jak nazwa, modul
i docstring. To wazne, bo bez `wraps` dekorowana funkcja traci czesc
swojej tozsamosci i trudniej ja analizowac albo dokumentowac.

Najwazniejsze elementy skladni w tym przykladzie to `def` z funkcja
zagniezdzona, dekorator `@dekorator`, gwiazdkowe argumenty `*args`
i `**kwargs` oraz blok `if __name__ == "__main__":`, ktory oddziela
kod demonstracyjny od definicji importowalnych.
"""

import functools
def dekorator(f_oryginalna):
    @functools.wraps(f_oryginalna)
    def f_nowa(*args, **kwargs):
        print('przed wywołaniem f_originalna')
        w = f_oryginalna(*args, **kwargs)
        print('po wywołaniu f_originalna')
        return w
    print('dekoruję', f_oryginalna)
    return f_nowa

if __name__ == "__main__":
    @dekorator
    def f1():
        print('f1')
        return 55

    # f1 = dekorator(f1)

    print(f1)
    f1()
