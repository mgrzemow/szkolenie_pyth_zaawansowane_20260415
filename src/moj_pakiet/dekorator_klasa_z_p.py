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


@dekorator(11, 22)
def f1():
    print('f1')
    return 55

# f1 = dekorator(f1)


print(f1)
f1()