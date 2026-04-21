"""
Demonstracja wyrażeń listowych, słownikowych i zbiorowych.

Pokazuje, jak typowe pętle budujące nowe kolekcje można zapisać krócej
i czytelniej za pomocą comprehension.
"""

from pprint import pprint


if __name__ == "__main__":
    # Klasyczna pętla budująca listę z filtrowaniem i transformacją.
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i**2)
    print(y)

    # Ta sama operacja zapisana jako list comprehension.
    print([i**2
           for i in x
           if i % 2 == 0])

    x = 'ala alicja alina paweł'
    # Lista wartości True/False informująca, czy słowo kończy się na 'a'.
    y = [slowo.endswith('a') for slowo in x.split()]
    print(all(y))
    print(any(y))

    # Gdy wynik jest zużywany od razu, można podać generator bez listy pośredniej.
    print(all(slowo.endswith('a') for slowo in x.split()))
    print(any(slowo.endswith('a') for slowo in x.split()))

    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Klasyczne spłaszczenie listy list.
    y = []
    for wiersz in x:
        for e in wiersz:
            y.append(e)
    print(y)

    # To samo spłaszczenie zapisane jako list comprehension.
    print([e for wiersz in x for e in wiersz])

    # Budowa tabliczki mnożenia w wersji imperatywnej.
    n = 7
    m = 5
    tabliczka = []
    for i in range(1, n + 1):
        wiersz = []
        for j in range(1, m + 1):
            wiersz.append(i * j)
        tabliczka.append(wiersz)
    pprint(tabliczka)

    # To samo jako zagnieżdżone list comprehension.
    tabliczka = [[i * j for j in range(1, m + 1)]
                 for i in range(1, n + 1)]
    pprint(tabliczka)

    x = 'ala alicja alina paweł'
    # Dict comprehension: słowo mapowane na długość.
    slownik = {slowo: len(slowo) for slowo in x.split()}
    pprint(slownik)

    # Set comprehension: unikalne pierwsze litery słów.
    zbior = {slowo[0] for slowo in x.split()}
    pprint(zbior)
