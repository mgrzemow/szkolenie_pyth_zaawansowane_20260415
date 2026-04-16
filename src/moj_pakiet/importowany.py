"""Moduł pomocniczy do pokazywania podstaw działania importów w Pythonie.

Ten plik jest celowo bardzo prosty, bo ma służyć jako materiał dydaktyczny
do omawiania zachowania modułów podczas importu i uruchamiania skryptu.

Najważniejsze idee pokazane na tym przykładzie:

- gdy plik jest **importowany**, Python ustawia w nim zmienną ``__name__``
  na nazwę modułu, np. ``"moj_pakiet.importowany"``,
- gdy ten sam plik jest uruchamiany **bezpośrednio**, Python ustawia
  ``__name__ == "__main__"``,
- dzięki temu blok:

  ```python
  if __name__ == "__main__":
      ...
  ```

  wykonuje się tylko przy bezpośrednim uruchomieniu pliku, a nie podczas importu.

To ważne, bo pozwala oddzielić:

- definicje funkcji, klas i stałych, które mają być dostępne po imporcie,
- kod demonstracyjny lub testowy, który nie powinien uruchamiać się jako efekt
  uboczny samego importu.

W praktyce standardowy mechanizm importu wykonuje kod modułu tylko raz
w ramach jednego procesu Pythona dla danej nazwy modułu, ponieważ załadowany
moduł trafia do cache ``sys.modules``. Kolejne importy tej samej nazwy zwykle
korzystają już z obiektu znajdującego się w pamięci, zamiast ponownie wykonywać
kod z pliku.

Dokumentacja Python:

- [__main__ — Top-level code environment](https://docs.python.org/3/library/__main__.html)
- [The import system](https://docs.python.org/3/reference/import.html)
- [sys.modules](https://docs.python.org/3/library/sys.html#sys.modules)
"""


def f1():
    """Wypisuje nazwę funkcji i bieżącą wartość ``__name__`` modułu.

    To prosty przykład pozwalający zobaczyć, czy moduł działa jako importowany
    moduł pakietu, czy jako plik uruchomiony bezpośrednio.
    """
    print("importowany.f1", __name__)


if __name__ == "__main__":
    print("kod globalny modułu importowanego", __name__)
