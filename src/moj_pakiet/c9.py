"""
Demonstracja dekoratora logującego opartego na module `logging`.

Plik pokazuje trzy powiązane elementy:

- minimalną konfigurację logowania przez `logging.basicConfig`,
- pobieranie loggera przypisanego do bieżącego modułu przez `getLogger(__name__)`,
- dekorator, który loguje poprawne wywołania funkcji oraz wyjątki.

Ważna idea w module `logging` jest taka, że nazwy loggerów tworzą hierarchię
opartą na kropkach, podobnie jak nazwy modułów Pythona. Logger o nazwie
`"pakiet.modul"` jest potomkiem loggera `"pakiet"`, a ten z kolei potomkiem
loggera głównego. Dzięki temu logger może dziedziczyć ustawienia swoich
przodków, np. poziom logowania, handlery i propagację zdarzeń, jeśli sam
nie ma własnej konfiguracji.

Dlatego wygodnie jest pobierać logger przez `logging.getLogger(__name__)`:

- nazwa loggera automatycznie odpowiada nazwie bieżącego modułu,
- nie trzeba ręcznie pilnować nazw w wielu plikach,
- loggery z różnych modułów naturalnie układają się w jedną hierarchię,
- centralna konfiguracja może później sterować całym pakietem lub jego częścią.

Pokazana konfiguracja jest celowo minimalna i nadaje się głównie do
demonstracji mechanizmu. W praktycznych projektach zwykle stosuje się
bogatszą, centralnie zarządzaną konfigurację logowania.
"""

import functools
import logging
from typing import Any

# Napisać dekorator logujący.

# To bardzo mała konfiguracja przykładowa: jeden plik, jeden poziom i podstawowy
# format ustawiony przez `basicConfig`. W realnej aplikacji zwykle konfiguruje się
# logowanie szerzej i w jednym miejscu startowym programu.
logging.basicConfig(
    filename="moj.log", filemode="wt", encoding="utf8", level=logging.DEBUG
)

# `__name__` daje nazwę bieżącego modułu, więc logger automatycznie trafia
# we właściwe miejsce hierarchii loggerów.
lgr = logging.getLogger(__name__)

# Gdyby istniały loggery o nazwach `xxx` i `xxx.yyy`, to `xxx.yyy` byłby
# potomkiem `xxx` i mógłby dziedziczyć jego ustawienia.
# xxx
# xxx.yyy
lgr.log(logging.WARNING, "ostrzezenie")


class dekorator_logujacy:
    def __init__(self, ok_level=logging.DEBUG, error_level=logging.ERROR) -> None:
        self.ok_level = ok_level
        self.error_level = error_level

    def __call__(self, f_oryginalna) -> Any:
        @functools.wraps(f_oryginalna)
        def f_nowa(*args, **kwargs):
            # Ponownie pobieramy logger modułu, aby wpisy trafiały do tego samego
            # miejsca w hierarchii loggerów.
            lgr = logging.getLogger(__name__)
            lgr.log(self.ok_level, f"{f_oryginalna.__name__}({args=}, {kwargs=})")
            try:
                w = f_oryginalna(*args, **kwargs)
            except BaseException as e:
                lgr.log(
                    self.error_level,
                    f"{f_oryginalna.__name__}({args=}, {kwargs=}), exception {e.__class__.__name__}: {e}, {e.args=}",
                )
                raise

            # Po poprawnym wykonaniu zapisujemy wynik funkcji.
            lgr.log(
                self.ok_level,
                f"{f_oryginalna.__name__}({args=}, {kwargs=}) -> {repr(w)}",
            )
            return w

        return f_nowa


@dekorator_logujacy(ok_level=logging.DEBUG, error_level=logging.ERROR)
def podziel(x, y):
    return x / y


if __name__ == "__main__":
    podziel(1, 2)
    podziel(1, 0)
