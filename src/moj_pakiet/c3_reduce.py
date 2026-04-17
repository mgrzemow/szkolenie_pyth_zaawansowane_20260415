import collections
from collections.abc import Mapping
import functools
from pathlib import Path


RESOURCE_FILE = Path(__file__).resolve().parents[2] / "resources" / "emaile.txt"


def wczytaj_emaile_po_domenach(plik_emaili: Path = RESOURCE_FILE) -> Mapping[str, set[str]]:
    slownik_rekordow: dict[str, set[str]] = collections.defaultdict(set)

    with plik_emaili.open("rt", encoding="utf8") as f:
        g1 = (linia.lower().strip() for linia in f)
        g2 = (linia for linia in g1 if "@" in linia)

        def f_agg(d, linia):
            _, domena = linia.split("@")
            d[domena].add(linia)
            return d

        slownik_rekordow = functools.reduce(f_agg, g2, collections.defaultdict(set))
    print(slownik_rekordow) 
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
