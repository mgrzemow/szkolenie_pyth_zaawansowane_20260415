"""
Demonstracja działania context managerów w Pythonie.

Plik pokazuje dwa podstawowe zastosowania protokołu context manager:

- prosty obiekt z metodami ``__enter__`` i ``__exit__``,
- praktyczny context manager mierzący czas wykonania bloku ``with``.

Najważniejsze idee tego przykładu:

- wejście do bloku ``with`` wywołuje ``__enter__``,
- wyjście z bloku, także po wyjątku, wywołuje ``__exit__``,
- ``__exit__`` może zdecydować, czy wyjątek ma zostać stłumiony,
- context manager nadaje się do zarządzania zasobami i do kodu pomocniczego,
  np. pomiaru czasu wykonania.
"""

# `contextlib` zawiera pomocne dodatki do pracy z context managerami,
# np. dekoratory i gotowe narzędzia do budowy własnych managerów kontekstu.
import contextlib
from typing import Any


# Minimalny przykład pokazujący sam mechanizm `__enter__` / `__exit__`.
class A:
    def __enter__(self):
        print("__enter__")
        # Obiekt zwrócony tutaj trafi do zmiennej po `as`, np. `with A() as alias:`.
        return self

    def __exit__(self, exc_type, exc, tb):
        # Parametry niosą informację o ewentualnym wyjątku z wnętrza bloku `with`.
        print("__exit__", exc_type, exc, tb)


# obiekt = A()
# print('kod przed with')
# with A() as alias:
#     print('kod pod with', alias)
#     x = 9/0

# print('kod poza with')

import time
# time.perf_counter()


# Praktyczny context manager do pomiaru czasu wykonania bloku `with`.
class Stoper:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        # Start pomiaru następuje dokładnie przy wejściu do bloku `with`.
        self.t1 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        print("__exit__", exc)
        self.t2 = time.perf_counter()
        # Zwrócenie `True` powoduje stłumienie wyjątku na potrzeby demonstracji.
        return True

    def __repr__(self) -> str:
        # Dzięki temu po wyjściu z bloku można wygodnie wypisać wynik pomiaru.
        return f"{self.nazwa}: {self.t2 - self.t1:.2f}s."


if __name__ == "__main__":
    # Ten przykład pokazuje, że `__exit__` wykona się nawet wtedy,
    # gdy wewnątrz bloku wystąpi wyjątek.
    with Stoper("100 000 insertow") as s:
        x = []
        for i in range(100_000):
            x.insert(0, i)
        x = 9 / 0

    print(s)  # 100 000 insertow : 4.67 s.
