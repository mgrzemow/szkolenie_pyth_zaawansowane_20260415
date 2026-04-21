"""
Demonstracja wyrażeń generatorowych.

Kolejne etapy przetwarzania nie tworzą od razu pełnych list w pamięci,
tylko produkują wartości leniwie, dopiero wtedy, gdy są potrzebne.
"""


if __name__ == "__main__":
    # Źródłem danych jest duża sekwencja, ale sama `range` też nie trzyma
    # wszystkich liczb jako gotowej listy w pamięci.
    x = range(10_000_000)
    input("stop")

    # Pierwsze wyrażenie generatorowe tworzy pipeline obliczeń, a nie wynik.
    y1 = (i**2 for i in x)
    input("stop")

    # Drugie wyrażenie generatorowe dokłada kolejny etap leniwego przetwarzania.
    y2 = (i / 14 for i in y1)
    input("stop")

    # Wartości są liczone dopiero podczas iteracji i tylko do momentu `break`.
    for i in y2:
        if i > 1000:
            break
        print(i)
