"""
Demonstracja dekorowania calej klasy zamiast pojedynczej funkcji.

Intencja tego modulu jest pokazanie, ze obiekt klasy po utworzeniu
tez mozna potraktowac jako argument dekoratora i zmodyfikowac go przed
oddaniem do dalszego uzycia. W praktyce dekorator klasy pozwala dodac
nowe atrybuty, metody albo zmienic istniejace elementy klasy.

Przyklad laczy dwa poziomy dekorowania:

- `dekorator_f` opakowuje pojedyncza funkcje lub metode,
- `dekorator_k` przyjmuje cala klase i modyfikuje jej zawartosc.

W klasie dekorator ustawia dodatkowy atrybut `version`, dynamicznie
dopisuje metode `m1` i warunkowo opakowuje metode `m2` drugim
dekoratorem. Dzieki temu dobrze widac, ze klasa jest zwyklym obiektem,
ktoremu mozna dopisywac elementy juz po wykonaniu instrukcji `class`.

Najwazniejsze elementy skladni to `@dekorator_k` nad definicja klasy,
wewnetrzna definicja funkcji `m1`, sprawdzanie `hasattr`, przypisanie
`cls.m1 = m1` oraz normalna instancjacja klasy po dekorowaniu.

To dobry plik do omowienia granicy miedzy metaprogramowaniem lekkim
a ciezszymi narzedziami takimi jak metaklasy. W wielu prostych
przypadkach dekorator klasy wystarcza i jest czytelniejszy.
"""

import functools
def dekorator_f(f_oryginalna):
    @functools.wraps(f_oryginalna)
    def f_nowa(*args, **kwargs):
        print('przed wywołaniem f_originalna')
        w = f_oryginalna(*args, **kwargs)
        print('po wywołaniu f_originalna')
        return w
    print('dekoruję', f_oryginalna)
    return f_nowa

def dekorator_k(cls):
    print('dekoruję klasę:', cls)
    cls.version = '1.2.3'
    def m1(self, x, y):
        return x + y
    cls.m1 = m1
    if hasattr(cls, 'm2'):
        cls.m2 = dekorator_f(cls.m2)
    return cls

if __name__ == "__main__":
    @dekorator_k
    class A:
        def m2(self):
            print('A. m2')

    a = A()
    print(a.version)
    print(a.m1(1, 2))
    print(a.m2())
