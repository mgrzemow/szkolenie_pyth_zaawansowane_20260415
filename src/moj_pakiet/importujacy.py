"""Moduł pokazujący importowanie innego modułu z pakietu.

Ten przykład służy do omówienia kilku ważnych zasad pracy z importami:

1. Import modułu wykonuje kod globalny modułu importowanego tylko przy
   pierwszym załadowaniu danej nazwy modułu w normalnym mechanizmie importu.
   Python przechowuje już załadowane moduły w ``sys.modules``, więc kolejne
   importy tej samej nazwy zwykle nie wykonują ponownie całego pliku.

2. To właśnie dlatego warto umieszczać kod demonstracyjny pod warunkiem
   ``if __name__ == "__main__":``. Taki kod wykona się przy bezpośrednim
   uruchomieniu pliku, ale nie jako efekt uboczny zwykłego importu.

3. Konstrukcja ``import *`` jest problematyczna dydaktycznie i praktycznie,
   ponieważ:

   - zaciera informację, skąd pochodzi dana nazwa,
   - może nadpisać istniejące nazwy w bieżącym module,
   - utrudnia czytanie kodu, analizę statyczną i autouzupełnianie.

W tym pliku użyty jest jawny import modułu:

```python
import moj_pakiet.importowany
```

Taki zapis jest czytelny, bo od razu widać, z jakiego modułu pochodzi wywołanie
``moj_pakiet.importowany.f1()``.

Dokumentacja Python:

- [The import system](https://docs.python.org/3/reference/import.html)
- [__main__ — Top-level code environment](https://docs.python.org/3/library/__main__.html)
- [import statement](https://docs.python.org/3/reference/simple_stmts.html#import)
"""


import moj_pakiet.importowany

moj_pakiet.importowany.f1()
