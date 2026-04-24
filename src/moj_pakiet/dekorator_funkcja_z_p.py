"""
Demonstracja dekoratora funkcyjnego z parametrami.

Intencja tego pliku jest pokazanie, ze dekorator moze miec wlasna
konfiguracje przekazywana przed otrzymaniem dekorowanej funkcji.
W praktyce oznacza to dodatkowy poziom zagniezdzenia: najpierw
wywolywana jest funkcja-fabryka dekoratora, a dopiero potem funkcja
wlasciwie dekorujaca.

Przyklad pokazuje klasyczny uklad trzech warstw:

- zewnetrzna funkcja `dekorator(p1, p2)` przyjmuje parametry,
- wewnetrzna funkcja `dekorator_wlasciwy` przyjmuje funkcje oryginalna,
- najglebsza funkcja `f_nowa` wykonuje kod przy wywolaniu.

To dobry material do omowienia domkniec, bo parametry `p1` i `p2`
pozostaja dostepne wewnatrz funkcji opakowujacej nawet po zakonczeniu
pracy funkcji zewnetrznej. Wlasnie dlatego mozliwe jest "zapamietanie"
konfiguracji dekoratora bez tworzenia osobnej klasy.

Najwazniejsze elementy skladni to `@dekorator(12, 33)`, funkcje
zagniezdzone, `functools.wraps`, argumenty `*args` i `**kwargs`
oraz zwracanie funkcji jako wartosci. Plik dobrze nadaje sie do
porownania z dekoratorem bez parametrow, bo roznica lezy glownie
w dodatkowym poziomie opakowania i czasie, w ktorym wykonywany jest
kod dekoratora.
"""

import functools


def dekorator(p1, p2):
    def dekorator_wlasciwy(f_oryginalna):
        @functools.wraps(f_oryginalna)
        def f_nowa(*args, **kwargs):
            print('przed wywołaniem f_originalna', p1, p2)
            w = f_oryginalna(*args, **kwargs)
            print('po wywołaniu f_originalna')
            return w
        print('dekoruję', f_oryginalna)
        return f_nowa
    return dekorator_wlasciwy

if __name__ == "__main__":
    @dekorator(12, 33)
    def f1():
        print('f1')
        return 55

    # f1 = dekorator(f1)

    print(f1)
    f1()
