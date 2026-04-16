"""Podstawy pętli w Pythonie.

Ten moduł porządkuje podstawowe informacje o pętlach ``while`` i ``for``.

## Pętla ``while``

Pętla ``while`` wykonuje blok kodu tak długo, jak długo warunek pozostaje
prawdziwy. Używa się jej wtedy, gdy liczba iteracji nie jest z góry znana,
albo gdy pętla ma działać do spełnienia określonego warunku.

## Pętla ``for``

Pętla ``for`` w Pythonie nie działa na zasadzie klasycznego licznika znanego
z wielu innych języków. Iteruje po elementach obiektu iterowalnego, np.:

- napisu,
- listy,
- krotki,
- zakresu zwracanego przez ``range(...)``,
- pliku czytanego linia po linii.

## Operator walrus ``:=``

Operator walrus pozwala przypisać wartość wewnątrz wyrażenia. Bywa przydatny
np. w pętlach ``while`` albo wtedy, gdy chcemy jednocześnie obliczyć wartość
i od razu z niej skorzystać.

## Dokumentacja Python

- [The while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [The for statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
- [range](https://docs.python.org/3/library/stdtypes.html#ranges)
- [Assignment expressions](https://docs.python.org/3/reference/expressions.html#assignment-expressions)
"""


if __name__ == "__main__":
    from pathlib import Path

    # Podstawowa pętla ``while`` z licznikiem.
    i = 0
    while i < 3:
        print(i)
        i += 1

    # Interaktywny przykład z operatorem walrus.
    # Zostawiamy go jako komentarz, żeby uruchomienie pliku nie blokowało się na ``input``.
    #
    # while (imie := input("Podaj imię: ")) != "koniec":
    #     print(f"Cześć {imie}")

    # Operator walrus może też zapisać wynik pośredni wewnątrz wyrażenia.
    r = 10
    h = 10
    v = (s := 3.14 * r * r) * h
    print(s, v)

    # Pętla ``for`` iteruje po wszystkich elementach napisu.
    for znak in "abc":
        print(znak)

    # Pętla ``for`` może iterować po elementach listy.
    for liczba in [1, 2, 3, 4, 5]:
        print(liczba)

    # ``range`` jest podstawowym sposobem wykonywania pętli określoną liczbę razy.
    for liczba in range(3):
        print("range:", liczba)

    # ``enumerate`` daje jednocześnie indeks i wartość.
    for indeks, znak in enumerate("abc"):
        print(indeks, znak)

    # Pętla ``for`` może czytać plik linia po linii.
    plik = Path(__file__).with_name("liczby.py")
    with plik.open("rt", encoding="utf8") as f:
        for linia in f:
            print(repr(linia))
