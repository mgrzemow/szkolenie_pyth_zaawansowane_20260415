"""
# Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Pogrupować adresy email po domenach, jedncześnie pozbywając się duplikatów. Proponuję format:

```python
{
'gmail.com': {'ala@gmail.com', 'ela@gmail.com'}
...
}
```

3. Zapisujemy adresy email do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   np wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt

## Podpowiedzi:

- nazwę domeny można wyciąć z adresu znajdując znak @
"""

import collections
from collections.abc import Mapping
from pathlib import Path
from pprint import pprint

RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "emaile.txt"
AdresyPoDomenach = collections.defaultdict[str, set[str]]
WidokAdresowPoDomenach = Mapping[str, set[str]]

def wczytaj_emaile_po_domenach(plik_emaili: Path = RESOURCE_FILE) -> AdresyPoDomenach:
    """Wczytuje adresy email z pliku i grupuje je po domenach.

    Funkcja przetwarza plik tekstowy linia po linii i buduje ``defaultdict``,
    w którym:

    - kluczem jest nazwa domeny,
    - wartością jest zbiór adresów email przypisanych do tej domeny.

    Niejawne reguły przetwarzania w obecnym rozwiązaniu są następujące:

    - każda linia jest sprowadzana do małych liter przez ``lower()``,
    - białe znaki na początku i końcu linii są usuwane przez ``strip()``,
    - przetwarzane są tylko linie zawierające znak ``@``,
    - duplikaty są usuwane automatycznie, ponieważ adresy trafiają do ``set``.

    Funkcja nie waliduje pełnej poprawności składni adresu email. Obecna logika
    uznaje za poprawny każdy wiersz zawierający znak ``@`` i rozdziela go na
    część lokalną oraz domenę przez ``split("@")``.

    Args:
        plik_emaili: Ścieżka do pliku z adresami email.

    Returns:
        ``defaultdict`` mapujący nazwę domeny na zbiór unikalnych adresów email.

    Raises:
        FileNotFoundError: Gdy wskazany plik wejściowy nie istnieje.
        ValueError: Gdy linia zawiera więcej niż jeden znak ``@`` i nie daje się
            rozpakować do dwóch części.

    See Also:
        - [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)
        - [set](https://docs.python.org/3/library/stdtypes.html#set)
    """
    slownik_rekordow: AdresyPoDomenach = collections.defaultdict(set)

    with plik_emaili.open("rt", encoding="utf8") as f:
        for linia in f:
            # Normalizujemy zapis, aby adresy różniły się tylko treścią, a nie wielkością liter.
            linia = linia.lower().strip()
            if "@" in linia:
                _, domena = linia.split("@")
                slownik_rekordow[domena].add(linia)

    return slownik_rekordow


def zapisz_emaile_po_domenach(
    adresy_po_domenach: WidokAdresowPoDomenach,
    katalog_docelowy: Path = RESOURCE_FILE.parent,
) -> None:
    """Zapisuje pogrupowane adresy email do osobnych plików domenowych.

    Dla każdej domeny tworzony jest osobny plik tekstowy o nazwie
    ``<domena>.txt``. Każdy adres email zapisywany jest w osobnym wierszu.

    Niejawne reguły biznesowe obecnego rozwiązania:

    - nazwa pliku wynika bezpośrednio z nazwy domeny,
    - pliki są zapisywane w katalogu docelowym przekazanym do funkcji,
    - kolejność adresów w plikach nie jest gwarantowana, ponieważ dane
      pochodzą ze zbiorów ``set``.

    Args:
        adresy_po_domenach: Mapowanie domen na zbiory unikalnych adresów email.
        katalog_docelowy: Katalog, w którym mają zostać utworzone pliki wynikowe.

    Returns:
        ``None``. Funkcja wykonuje zapis do plików jako efekt uboczny.
    """
    for domena, emaile in adresy_po_domenach.items():
        # Każda domena trafia do osobnego pliku tekstowego.
        with (katalog_docelowy / f"{domena}.txt").open("wt", encoding="utf8") as f:
            for email in emaile:
                f.write(email + "\n")


if __name__ == "__main__":
    slownik_rekordow = wczytaj_emaile_po_domenach()
    zapisz_emaile_po_domenach(slownik_rekordow)
