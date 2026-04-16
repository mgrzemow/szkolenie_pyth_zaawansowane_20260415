"""
Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Pogrupować adresy email po domenach, jedncześnie pozbywając się duplikatów. Proponuję format:
{
'gmail.com': {'ala@gmail.com', 'ela@gmail.com'}
...
}
3. Zapisujemy adresy email do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   np wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt

Podpowiedzi:
 - nazwę domeny można wyciąć z adresu znajdując znak @
"""

from collections.abc import Mapping
from pathlib import Path


RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "emaile.txt"


def wczytaj_emaile_po_domenach(plik_emaili: Path = RESOURCE_FILE) -> Mapping[str, set[str]]:
    """Wczytuje adresy email z pliku i grupuje je po domenach.

    Funkcja przetwarza plik tekstowy linia po linii i buduje słownik, w którym:

    - kluczem jest nazwa domeny,
    - wartością jest zbiór unikalnych adresów email dla tej domeny.

    Niejawne reguły obecnego rozwiązania:

    - każdy adres jest normalizowany przez ``lower().strip()``,
    - przetwarzane są tylko linie zawierające znak ``@``,
    - duplikaty są usuwane dzięki użyciu ``set``,
    - domena jest wyznaczana przez rozdzielenie tekstu po znaku ``@``.

    Funkcja nie waliduje pełnej poprawności adresu email. W obecnym modelu
    wystarcza sama obecność znaku ``@``.

    Args:
        plik_emaili: Ścieżka do pliku z adresami email.

    Returns:
        Mapowanie domen na zbiory unikalnych adresów email.

    Raises:
        FileNotFoundError: Gdy wskazany plik wejściowy nie istnieje.
        ValueError: Gdy linia zawiera więcej niż jeden znak ``@`` i nie daje się
            rozpakować do dwóch części.

    See Also:
        - [set](https://docs.python.org/3/library/stdtypes.html#set)
        - [dict](https://docs.python.org/3/library/stdtypes.html#dict)
    """
    slownik_rekordow: dict[str, set[str]] = {}

    with plik_emaili.open("rt", encoding="utf8") as f:
        for linia in f:
            # Ujednolicamy zapis, aby różnice w wielkości liter nie tworzyły duplikatów.
            linia = linia.lower().strip()
            if "@" in linia:
                _, domena = linia.split("@")
                if domena not in slownik_rekordow:
                    slownik_rekordow[domena] = set()
                slownik_rekordow[domena].add(linia)

    return slownik_rekordow


def zapisz_emaile_po_domenach(
    adresy_po_domenach: Mapping[str, set[str]],
    katalog_docelowy: Path = RESOURCE_FILE.parent,
) -> None:
    """Zapisuje adresy email do osobnych plików nazwanych od domen.

    Dla każdej domeny funkcja tworzy osobny plik tekstowy w formacie
    ``<domena>.txt`` i zapisuje w nim wszystkie przypisane adresy email,
    po jednym w wierszu.

    Niejawne reguły obecnego rozwiązania:

    - nazwa pliku wynika bezpośrednio z nazwy domeny,
    - pliki są zapisywane w katalogu przekazanym w argumencie,
    - kolejność adresów w pliku nie jest gwarantowana, ponieważ źródłem danych
      jest zbiór ``set``.

    Args:
        adresy_po_domenach: Mapowanie domen na zbiory unikalnych adresów email.
        katalog_docelowy: Katalog, do którego mają zostać zapisane pliki wynikowe.

    Returns:
        ``None``. Funkcja zapisuje dane do plików jako efekt uboczny.
    """
    for domena, emaile in adresy_po_domenach.items():
        # Każda domena trafia do własnego pliku tekstowego.
        with (katalog_docelowy / f"{domena}.txt").open("wt", encoding="utf8") as f:
            for email in emaile:
                f.write(email + "\n")


if __name__ == "__main__":
    slownik_rekordow = wczytaj_emaile_po_domenach()
    zapisz_emaile_po_domenach(slownik_rekordow)
