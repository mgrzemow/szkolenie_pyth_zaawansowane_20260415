"""Przyklady obslugi wyjatkow w Pythonie.

Modul pokazuje podstawowe i rozszerzone elementy obslugi bledow w Pythonie
na jednym, niewielkim przykladzie. Kod demonstruje:

- przechwytywanie konkretnych wyjatkow przy pomocy ``except``,
- przechwytywanie bledow ogolnych przy pomocy ``except Exception``,
- blok ``else`` uruchamiany tylko wtedy, gdy w ``try`` nie wystapi zaden wyjatek,
- blok ``finally`` uruchamiany zawsze, niezaleznie od powodzenia lub bledu,
- ponowne zglaszanie bledu przy pomocy ``raise``,
- wypisywanie pelnego stack trace przy pomocy modulu ``traceback``.

W Pythonie wyjatki sa zwyklymi obiektami dziedziczacymi po klasie
``BaseException``. W praktyce aplikacyjnej najczesciej przechwytuje sie klasy
dziedziczace po ``Exception``. Pozwala to obsluzyc przewidywalne problemy,
takie jak:

- dzielenie przez zero,
- odwolanie do elementu spoza zakresu listy,
- brak pliku na dysku,
- niepoprawne dane wejsciowe.

Warto rozrozniac dwa poziomy obslugi bledow:

1. **obsluga lokalna** - blisko miejsca, w ktorym blad moze wystapic,
2. **obsluga globalna** - na granicy programu, gdzie logujemy blad
   i wypisujemy diagnostyke.

Ten modul pokazuje oba podejscia jednoczesnie. Funkcja ``main()`` obsluguje
wybrane bledy lokalnie, a kod uruchamiany w bloku ``if __name__ == "__main__"``
pokazuje, jak wypisac pelny stos wywolan dla nieobsluzonego lub ponownie
zgloszonego wyjatku.

Dokumentacja Python:

- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [traceback — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
"""

import traceback


def main() -> None:
    """Uruchamia przyklad pokazujacy rozne sciezki obslugi wyjatkow.

    Funkcja wykonuje kilka operacji, ktore moga zakonczyc sie bledem:

    - pobranie elementu listy po indeksie,
    - dzielenie przez element listy,
    - otwarcie pliku z dysku.

    Wewnatrz ``try`` znajduja sie operacje ryzykowne, a kolejne bloki
    ``except`` przechwytuja rozne typy wyjatkow:

    - ``ZeroDivisionError`` dla dzielenia przez zero,
    - ``IndexError`` dla niepoprawnego indeksu listy,
    - ``FileNotFoundError`` dla braku pliku,
    - ``Exception`` jako zabezpieczenie ogolne.

    Blok ``else`` wykonuje sie tylko wtedy, gdy nie wystapi zaden wyjatek.
    Blok ``finally`` wykonuje sie zawsze i nadaje sie do sprzatania zasobow
    lub wypisywania informacji koncowych.

    Returns:
        Nic nie zwraca. Funkcja sluzy do demonstracji zachowania programu
        przy obsludze bledow.

    Raises:
        ZeroDivisionError: Gdy wybrany element listy ma wartosc zero.
        IndexError: Gdy zmienna ``z`` wskazuje indeks spoza listy.
        FileNotFoundError: Gdy otwierany plik nie istnieje.
        Exception: Gdy wystapi inny, nieprzewidziany blad.
    """
    a = [1, 2, 3, 4, 0]
    z = 5

    try:
        x = 9 / a[z]
        open("asdasdasdasd")
    except ZeroDivisionError as e:
        print(f"Nie mozna dzielic przez zero: {e}, {a=}, {z=}")
        raise
    except IndexError as e:
        print(f"Niepoprawny indeks listy: {e}, {a=}, {z=}")
        raise
    except FileNotFoundError as e:
        print(f"Nie znaleziono pliku: {e}")
        raise
    except Exception as e:
        print(f"Wystapil nieoczekiwany blad w main(): {e.__class__.__name__}: {e}")
        raise
    else:
        print(f"Operacje zakonczyly sie powodzeniem, wynik dzielenia: {x}")
    finally:
        print("Blok finally w main() wykonany.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}, args: {e.args}")
        traceback.print_exc()
        raise
