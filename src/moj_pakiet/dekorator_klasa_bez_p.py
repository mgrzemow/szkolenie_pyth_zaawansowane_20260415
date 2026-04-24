"""
Demonstracja dekoratora zaimplementowanego jako klasa bez dodatkowych
parametrow konfiguracyjnych.

Plik pokazuje, ze dekorator nie musi byc funkcja. Moze nim byc takze
obiekt wywolywalny, czyli instancja klasy posiadajacej metode
`__call__`. Taki obiekt moze przechowywac stan i logike dekorowania
w atrybutach oraz metodach klasy.

Ten konkretny przyklad jest celowo pokazowy i sluzy do rozmowy o tym,
jak dekorowanie metod rozni sie od dekorowania zwyklych funkcji.
Pojawia sie tu temat przekazywania `self` oraz to, dlaczego przy
dekorowaniu metod trzeba rozumiec protokol deskryptora i metode
`__get__`.

Wykorzystane mechanizmy Pythona to:

- klasa jako dekorator,
- metoda specjalna `__call__`,
- metoda specjalna `__get__`,
- `functools.partial` do zwiazania instancji,
- dekorowanie metody przez skladnie `@dekorator`.

Najwazniejsze elementy skladni to definicja klasy z metodami
specjalnymi, adnotacja typu `-> Any`, uzycie `@dekorator` nad metoda
oraz blok `if __name__ == "__main__":` z mala demonstracja zachowania.
To nie jest wzorzec "najlepszy praktycznie", ale bardzo dobry do
analizy tego, jak Python obsluguje dostep do metod w obiektach.
"""

# Nie używać !!!
# problemy z przekazywaniem selfa do metody w klasie

import functools
from typing import Any


class dekorator:
    def __init__(self, f) -> None:
        self.f = f

    def __call__(self, *args, **kwargs) -> Any:
        print('przed wywołaniem f_originalna')
        w = self.f(*args, **kwargs)
        print('po wywołaniu f_originalna')
        return w

    def __get__(self, instance, owner):
        return functools.partial(self, instance)
        pass

if __name__ == "__main__":
    class A:
        @dekorator
        def f1(self):
            print('f1')
            return 55

    # f1 = dekorator(f1)
    a = A()

    a.f1()
