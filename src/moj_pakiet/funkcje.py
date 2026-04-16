"""Przykłady definiowania i wywoływania funkcji w Pythonie.

Moduł zbiera krótkie przykłady pokazujące najważniejsze elementy pracy
z funkcjami w Pythonie:

- definicję funkcji przez ``def``,
- bardzo proste funkcje z zerem, jednym i dwoma parametrami,
- różnicę między parametrem obowiązkowym a opcjonalnym,
- parametry pozycyjne i argumenty domyślne,
- ``*args`` i ``**kwargs``,
- argumenty tylko słowne,
- brak klasycznego overloadingu przez wielokrotne definicje tej samej nazwy,
- pułapkę mutowalnych wartości domyślnych,
- zasięgi nazw według reguły LEGB,
- domknięcia i późne wiązanie zmiennych w closure.

W Pythonie funkcja jest obiektem. Można ją przypisać do zmiennej, zwrócić
z innej funkcji i przekazać jako argument. Sama definicja funkcji nie uruchamia
jej kodu. Kod w ciele funkcji wykonuje się dopiero przy wywołaniu.

Warto pamiętać o kilku ważnych zasadach:

- Python nie wspiera klasycznego przeciążania funkcji tylko po liczbie lub typach
  argumentów. Druga definicja o tej samej nazwie nadpisuje pierwszą.
- Argumenty domyślne są obliczane raz, w chwili definiowania funkcji.
  Dlatego mutowalne wartości domyślne, takie jak ``[]`` czy ``{}``, mogą
  prowadzić do trudnych błędów.
- Parametry po ``*`` stają się argumentami tylko słownymi.
- ``*args`` zbiera nadmiarowe argumenty pozycyjne do krotki.
- ``**kwargs`` zbiera nadmiarowe argumenty nazwane do słownika.

Dokumentacja Python:

- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Special Parameters](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
- [Execution Model - Name Resolution](https://docs.python.org/3/reference/executionmodel.html#resolution-of-names)
"""


def przywitaj_swiat():
    """Pokazuje bardzo prostą funkcję bez parametrów.

    To najprostszy możliwy wariant: funkcja niczego nie przyjmuje
    i wykonuje jedną prostą operację.
    """
    print("Cześć!")


# Działające wywołanie:
# przywitaj_swiat()
#
# Błąd: funkcja nie przyjmuje żadnych argumentów.
# przywitaj_swiat("Ala")


def przywitaj_osobe(imie: str):
    """Pokazuje funkcję z jednym parametrem obowiązkowym.

    Parametr ``imie`` musi zostać przekazany przy każdym wywołaniu funkcji.
    """
    print(f"Cześć {imie}")


# Działające wywołanie:
# przywitaj_osobe("Ala")
#
# Błąd: brakuje wymaganego argumentu ``imie``.
# przywitaj_osobe()


def dodaj_dwie_liczby(a: int, b: int) -> int:
    """Pokazuje funkcję z dwoma parametrami obowiązkowymi.

    Oba parametry muszą zostać przekazane przy wywołaniu.
    Funkcja zwraca wynik, zamiast go wypisywać.
    """
    return a + b


# Działające wywołanie:
# wynik = dodaj_dwie_liczby(2, 3)
# print(wynik)
#
# Błąd: brakuje drugiego obowiązkowego argumentu ``b``.
# dodaj_dwie_liczby(2)


def przedstaw_osobe(imie: str, miasto: str = "Warszawa"):
    """Pokazuje różnicę między parametrem obowiązkowym a opcjonalnym.

    Parametr ``imie`` jest obowiązkowy, więc trzeba go podać zawsze.
    Parametr ``miasto`` jest opcjonalny, ponieważ ma wartość domyślną.
    Jeśli użytkownik go nie poda, funkcja użyje wartości ``"Warszawa"``.
    """
    print(f"{imie} mieszka w mieście {miasto}")


# Działające wywołania:
# przedstaw_osobe("Ala")
# przedstaw_osobe("Ala", "Kraków")
#
# Błąd: brakuje wymaganego argumentu ``imie``.
# przedstaw_osobe()


def f1():
    """Pokazuje najprostszą funkcję bez parametrów i bez jawnego ``return``.

    Funkcja jedynie wypisuje tekst. Ponieważ nie zawiera instrukcji ``return``,
    zwraca domyślnie ``None``.
    """
    print("f1")


# Działające wywołanie:
# w = f1()
# print(w)
#
# Błąd: funkcja nie przyjmuje żadnych argumentów.
# f1(1)


# Przykład metody, która modyfikuje listę w miejscu i zwraca ``None``.
x = [1, 5, 4, 5, 3, 5, 6, 7, 8, 9]
# y = x.sort()
# print(y)


# Nie ma klasycznego overloadingu. Druga definicja ``f2`` nadpisze pierwszą.
def f2(x, y):
    """Pierwsza wersja przykładu przeciążania, nadpisywana niżej.

    Ta definicja istnieje tylko po to, aby pokazać, że kolejna definicja
    funkcji o tej samej nazwie zastępuje poprzednią.
    """
    print("f2", x, y)


def f2(x):
    """Druga definicja ``f2``, która zastępuje wcześniejszą wersję.

    To właśnie ta wersja będzie dostępna pod nazwą ``f2`` po wczytaniu modułu.
    """
    print("f2", x)


# Czy da się to jakoś obejść?
# Tak, ale moim zdaniem nie zawsze jest to dobre rozwiązanie dydaktyczne.
# import functools
# Jeżeli chcę rozpoznawać wersję funkcji po typie pierwszego argumentu,
# to mogę użyć dekoratora ``functools.singledispatch``.
# Jeżeli chcę pełne overloading, to zwykle potrzebuję dodatkowej biblioteki,
# np. ``multimethod``.

# Działające wywołanie:
# f2(1)
#
# Błąd: po nadpisaniu funkcja oczekuje jednego argumentu.
# f2(1, 2)


def f3(x, y, *args, a=11, b=22, **kwargs):
    """Pokazuje jednoczesne użycie różnych rodzajów parametrów.

    Funkcja przyjmuje:

    - dwa zwykłe parametry pozycyjne,
    - dodatkowe argumenty pozycyjne przez ``*args``,
    - dwa parametry nazwane z wartościami domyślnymi,
    - dodatkowe argumenty nazwane przez ``**kwargs``.
    """
    print(f"{x=}, {y=}, {args=}, {a=}, {b=}, {kwargs=}")


# Działające wywołanie:
# f3(1, 2, 3, 4, 5, 6, b=222, c=333, d=444)
#
# Błąd: brakuje wymaganego argumentu pozycyjnego ``y``.
# f3(1)


def f4(x, y, a=11, b=22):
    """Pokazuje zwykłe argumenty domyślne.

    Parametry ``a`` i ``b`` mają wartości domyślne, więc można je pominąć
    przy wywołaniu.
    """
    print(f"{x=}, {y=}, {a=}, {b=}")


# Działające wywołanie:
# f4(1, 2, 3, 4)
#
# Błąd: brakuje wymaganego argumentu ``y``.
# f4(1)


def f5(x, y, *, a=11, b=22):
    """Pokazuje parametry tylko słowne po znaku ``*``.

    Parametry ``a`` i ``b`` nie mogą być przekazane pozycyjnie.
    """
    print(f"{x=}, {y=}, {a=}, {b=}")


# Działające wywołanie:
# f5(1, 2, a=3)
#
# Błąd: trzeci argument pozycyjny nie jest dozwolony.
# f5(1, 2, 3)


def f6(x, y, *, a, b):
    """Pokazuje wymagane argumenty tylko słowne.

    Parametry ``a`` i ``b`` są obowiązkowe, ale muszą być przekazane po nazwie.
    """
    print(f"{x=}, {y=}, {a=}, {b=}")


# Działające wywołanie:
# f6(1, 2, a=3, b=4)
#
# Błąd: brakuje wymaganych argumentów tylko słownych ``a`` i ``b``.
# f6(1, 2)


def f7(x, y):
    """Prosta funkcja z dwoma argumentami pozycyjnymi.

    Stanowi funkcję docelową dla przykładu przekazywania argumentów dalej
    przez ``*args``.
    """
    print(f"{x=}, {y=}")


def f7_1(z, *args):
    """Pokazuje przekazywanie argumentów pozycyjnych do innej funkcji.

    Parametr ``z`` jest obsługiwany lokalnie, a pozostałe argumenty trafiają
    dalej do ``f7``.
    """
    print(f"{z=}")
    f7(*args)


# Działające wywołanie:
# f7_1(1, 2, 3)
#
# Błąd: po przekazaniu dalej argumentów funkcji ``f7`` zabraknie ``y``.
# f7_1(1, 2)


def f8(*, x, y):
    """Pokazuje funkcję przyjmującą wyłącznie argumenty nazwane."""
    print(f"{x=}, {y=}")


def f8_1(*, z, **kwargs):
    """Pokazuje przekazywanie argumentów nazwanych dalej przez ``**kwargs``.

    Parametr ``z`` jest obsługiwany lokalnie, a pozostałe argumenty nazwane
    trafiają do funkcji ``f8``.
    """
    print(f"{z=}")
    f8(**kwargs)


# Działające wywołanie:
# f8_1(x=1, y=2, z=3)
#
# Błąd: po przekazaniu dalej argumentów zabraknie ``y`` dla ``f8``.
# f8_1(x=1, z=3)


def f9(i, x=[]):
    """Pokazuje pułapkę mutowalnej wartości domyślnej.

    Lista w parametrze domyślnym jest tworzona raz, w chwili definiowania
    funkcji, więc kolejne wywołania bez argumentu ``x`` współdzielą tę samą
    listę.
    """
    x.append(i)
    print(id(x), x)


# Działające wywołania:
# f9(1)
# f9(2)
# f9(3)


def f9(i, x=None):
    """Pokazuje poprawny sposób obsługi mutowalnej wartości domyślnej.

    Zamiast używać pustej listy w sygnaturze, funkcja przyjmuje ``None``
    i tworzy nową listę dopiero wewnątrz ciała funkcji.
    """
    if x is None:
        x = []
    x.append(i)
    print(x)


# Działające wywołania:
# f9(1)
# f9(2)
# f9(3)

x = 99


def f10():
    """Pokazuje lokalny zasięg zmiennej i zwracanie wartości z funkcji.

    Zmienna ``x`` zdefiniowana w środku funkcji nie jest tą samą zmienną,
    co globalne ``x`` z modułu.
    """
    x = 11
    return x


# Działające wywołanie:
# x = f10()
# print(x)
#
# Błąd: funkcja nie przyjmuje argumentów.
# f10(1)

# LEGB:
# Local
# Enclosing
# Global
# Built-in


# __name__ = "global name"
def f11():
    """Pokazuje odczyt nazwy według reguły LEGB.

    Wewnętrzna funkcja odwołuje się do ``__name__``, które ostatecznie
    zostaje znalezione w zakresie globalnym modułu.
    """

    # __name__ = "enclosing name"
    def f11_1():
        """Wewnętrzna funkcja używana do demonstracji wyszukiwania nazw."""

        # __name__ = "local name"
        print(__name__)

    f11_1()


# Działające wywołanie:
# f11()


def f12():
    """Zwraca funkcję wewnętrzną domykającą zmienne z zakresu zewnętrznego.

    To podstawowy przykład closure: funkcja zwracana pamięta wartości ``x`` i ``y``
    nawet po zakończeniu działania funkcji zewnętrznej.
    """
    x = "mama"
    y = "tata"

    def f12_1():
        """Funkcja wewnętrzna korzystająca ze zmiennych z closure."""

        print("f12_1", x, y)

    return f12_1


# Działające wywołania:
# f = f12()
# f()
# print(f.__closure__)
# print(f.__code__.co_freevars)


def f13():
    """Pokazuje problem późnego wiązania zmiennej w domknięciu.

    Wszystkie zwrócone funkcje odwołują się do tej samej zmiennej ``i``,
    więc po zakończeniu pętli widzą jej ostatnią wartość.
    """
    lista_funkcji = []
    for i in range(3):

        def f12_1():
            """Wewnętrzna funkcja pokazująca efekt późnego wiązania."""

            print(i)

        lista_funkcji.append(f12_1)

    # Uwaga: closure wiąże nazwę, a nie kopię aktualnej wartości z iteracji.
    return lista_funkcji


# Działające wywołania:
# lf = f13()
# for f in lf:
#     f()


def f13():
    """Pokazuje poprawkę problemu późnego wiązania przez parametr domyślny.

    Wartość ``i`` jest zapisywana do parametru domyślnego funkcji wewnętrznej,
    dzięki czemu każda zwracana funkcja pamięta własną wartość z iteracji.
    """
    lista_funkcji = []
    for i in range(3):

        def f12_1(i=i):
            """Wewnętrzna funkcja przechwytująca wartość z bieżącej iteracji."""

            print(i)

        lista_funkcji.append(f12_1)

    return lista_funkcji


# Działające wywołania:
# lf = f13()
# for f in lf:
#     f()


def print_n_razy(*args, n: int = 1, **kwargs) -> int:
    """Wypisuje przekazane argumenty zadaną liczbę razy.

    Funkcja łączy kilka technik:

    - ``*args`` zbiera argumenty pozycyjne do wypisania,
    - ``n`` steruje liczbą powtórzeń,
    - ``**kwargs`` przekazuje dodatkowe opcje dalej do ``print``.

    Args:
        *args: Argumenty pozycyjne przekazywane dalej do ``print``.
        n: Liczba powtórzeń.
        **kwargs: Dodatkowe argumenty nazwane dla funkcji ``print``.

    Returns:
        Liczbę wykonanych powtórzeń.
    """
    print(n)
    for _ in range(n):
        print(*args, **kwargs)
    return n


# Działające wywołanie:
# print_n_razy(1, 2, 3, n=3, sep=" - ", end="\n!!!\n")
#
# Błąd: ``range`` oczekuje liczby całkowitej, a nie napisu.
# print_n_razy(1, 2, 3, n="3")
