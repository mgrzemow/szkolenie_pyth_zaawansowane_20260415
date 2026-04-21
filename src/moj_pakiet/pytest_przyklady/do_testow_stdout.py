"""
Prosty moduł do demonstracji przechwytywania wyjścia w pytest.

Funkcje nie zwracają danych, tylko wypisują tekst na standardowe wyjście,
więc dobrze pokazują użycie fixture `capsys`.
"""


def wypisz_powitanie(imie):
    """Wypisuje prosty komunikat powitalny."""
    print(f"Czesc, {imie}!")


def wypisz_parzyste_liczby(granica):
    """Wypisuje liczby parzyste od zera do podanej granicy włącznie."""
    for liczba in range(granica + 1):
        if liczba % 2 == 0:
            print(liczba)


if __name__ == "__main__":
    # Prosty podgląd działania bez uruchamiania testów.
    wypisz_powitanie("Ala")
    wypisz_parzyste_liczby(6)
