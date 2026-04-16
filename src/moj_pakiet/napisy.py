"""Podstawy pracy z napisami w Pythonie.

Ten moduł porządkuje najważniejsze informacje o typie ``str`` i kilku
powiązanych zagadnieniach.

## Napisy typu ``str``

Napisy w Pythonie:

- są sekwencjami znaków Unicode,
- są niemutowalne, czyli nie można zmieniać pojedynczych znaków w miejscu,
- wspierają indeksowanie, slicing i iterowanie,
- mają wiele metod pomocniczych, takich jak ``split``, ``join``, ``strip``,
  ``upper`` czy ``lower``.

Ponieważ napisy są niemutowalne, większość operacji tekstowych zwraca nowy
obiekt zamiast modyfikować istniejący napis.

## Raw strings i byte strings

W praktyce warto odróżniać:

- ``str`` - zwykły napis tekstowy Unicode,
- ``r"..."`` - raw string, przydatny np. w wyrażeniach regularnych i ścieżkach,
- ``b"..."`` - byte string, czyli sekwencję bajtów, a nie napis Unicode.

## Formatowanie napisów

Najczęściej spotykane techniki budowania napisów to:

- f-stringi,
- ``str.format(...)``,
- ``"separator".join(...)`` dla łączenia wielu fragmentów tekstu.

## Dokumentacja Python

- [Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
- [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
"""


if __name__ == "__main__":
    # Raw string przydaje się np. do regexów, bo backslash nie jest tu
    # interpretowany w typowy sposób przez parser napisów.
    x = r"\d\d"
    print(x)

    # Byte string to sekwencja bajtów, a nie zwykły napis Unicode.
    x = b"abc"
    print(type(x))

    # Podstawowe operacje na napisach.
    x = "Ala ma kota"
    print(len(x))
    print(x[0])
    print(x[-1])
    print(x[0:3])

    # Konkatenacja napisów.
    imie = "Jan"
    nazwisko = "Nowak"
    print(imie + " " + nazwisko)

    # Formatowanie przy użyciu f-stringa.
    imie = "Jan"
    wiek = 45
    waga = 88.2343234234
    print(f">{imie:12}< ma {wiek} lat i waży {waga:.2f} kg.")

    # Ten sam wynik można budować także przez ``str.format``.
    waluta = "usd"
    url_szablon = "https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json"
    url = url_szablon.format(waluta)
    print(url)

    # F-string bywa czytelniejszy przy prostym podstawianiu zmiennych.
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json"
    print(url)

    # Indeksowanie i slicing.
    # Dla napisu długości n poprawne indeksy to 0 .. n-1 oraz -n .. -1.
    x = "abcdefgh"
    print(x[1:4])
    print(x[:3])
    print(x[-3:])
    print(x[:-3])
    print(x[3:])
    print(x[1:-1])
    print(x[::-1])

    # ``split`` rozbija napis na listę słów.
    x = "   \t   ala \t ma   kota\n"
    print(x.split())

    # ``strip`` usuwa białe znaki z początku i końca.
    print(x.strip())

    # Metody napisów zwykle zwracają nowy obiekt, bo ``str`` jest niemutowalny.
    x = "mama"
    y = x.upper()
    print(id(x), id(y))
    print(x is y)
    print(x, y)

    # Budowanie większego napisu z wielu fragmentów.
    x = "as"
    y = "dsad"
    z = "dsad"
    q = "asdasd"
    w = f"{x}{y}{z}{q}"
    print(w)

    # ``join`` to preferowany sposób łączenia listy napisów w jeden napis.
    lista_w = ["ala", "ma", "kota"]
    print(" - ".join(lista_w))

    # Sprawdzanie, czy fragment tekstu występuje w napisie.
    print("ma" in "ala ma kota")

    # Porównanie napisów bywa mylące, gdy w jednym z nich są ukryte białe znaki.
    x = "Ala"
    y = "Ala "
    print(x == y)
    print(repr(x), repr(y))
