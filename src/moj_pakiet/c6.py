import contextlib
from typing import Any


class A:
    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("__exit__", exc_type, exc, tb)


# obiekt = A()
# print('kod przed with')
# with A() as alias:
#     print('kod pod with', alias)
#     x = 9/0

# print('kod poza with')

import time
# time.perf_counter()


class Stoper:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        self.t1 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        print('__exit__', exc)
        self.t2 = time.perf_counter()
        # zwracane true blokuje propagację wyjatku
        return True

    def __repr__(self) -> str:
        return f"{self.nazwa}: {self.t2 - self.t1:.2f}s."


with Stoper("100 000 insertow") as s:
    x = []
    for i in range(100_000):
        x.insert(0, i)
    x = 9/0

print(s)  # 100 000 insertow : 4.67 s.
