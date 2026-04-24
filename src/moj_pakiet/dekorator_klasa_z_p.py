"""
Demonstracja dekoratora klasowego z parametrami.

Ten modul rozwija poprzedni wariant dekoratora-klasy i pokazuje,
jak polaczyc dwa pomysly:

- przechowywanie konfiguracji w instancji klasy dekoratora,
- zwracanie funkcji opakowujacej podczas dekorowania.

Przy dekorowaniu przez `@dekorator(11, 22)` najpierw tworzona jest
instancja klasy dekoratora z parametrami `p1` i `p2`. Dopiero potem
ta instancja otrzymuje dekorowana funkcje w metodzie `__call__`
i zwraca nowa funkcje opakowujaca.

Przyklad pokazuje tez praktyczna roznice miedzy "obiekt dekoratora"
a "funkcja wykonywana przy wywolaniu". Stan konfiguracyjny znajduje sie
w `self`, ale samo wywolanie dekorowanej funkcji obsluguje lokalna
funkcja `f_nowa`, zamknieta nad `self` i nad funkcja oryginalna.

Najwazniejsze mechanizmy i skladnia to:

- klasa z konstruktorem `__init__`,
- metoda specjalna `__call__`,
- `functools.wraps`,
- dekorowanie przez `@nazwa(argumenty)`,
- domkniecie pozwalajace korzystac z `self.p1` i `self.p2` wewnatrz
  funkcji opakowujacej.

To nadal kod demonstracyjny, ale dobrze pokazuje, kiedy wygodnie
przejsc z dekoratora funkcyjnego na dekorator oparty o klase.
"""

import functools
from typing import Any


class dekorator:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p1

    def __call__(self, f_oryginalna) -> Any:
        @functools.wraps(f_oryginalna)
        def f_nowa(*args, **kwargs):
            print('przed wywołaniem f_originalna', self.p1, self.p2)
            w = f_oryginalna(*args, **kwargs)
            print('po wywołaniu f_originalna')
            return w
        print('dekoruję', f_oryginalna)
        return f_nowa


if __name__ == "__main__":
    @dekorator(11, 22)
    def f1():
        print('f1')
        return 55

    # f1 = dekorator(f1)

    print(f1)
    f1()
