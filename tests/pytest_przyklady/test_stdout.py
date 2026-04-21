"""
Przykłady testów przechwytujących standardowe wyjście.

Fixture `capsys` pozwala odczytać to, co funkcja wypisała przez `print`.
"""

from moj_pakiet.pytest_przyklady.do_testow_stdout import (
    wypisz_parzyste_liczby,
    wypisz_powitanie,
)


def test_wypisz_powitanie(capsys):
    """Po wykonaniu funkcji odczytujemy bufor standardowego wyjścia."""
    wypisz_powitanie("Ala")

    # `readouterr` zwraca to, co zostało wypisane na stdout i stderr.
    captured = capsys.readouterr()
    assert captured.out == "Czesc, Ala!\n"


def test_wypisz_parzyste_liczby(capsys):
    """Test sprawdza kilka wypisanych linii naraz."""
    wypisz_parzyste_liczby(6)

    captured = capsys.readouterr()
    assert captured.out == "0\n2\n4\n6\n"
