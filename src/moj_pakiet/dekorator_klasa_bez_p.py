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

class A:
    @dekorator
    def f1(self):
        print('f1')
        return 55

# f1 = dekorator(f1)
a = A()

a.f1()