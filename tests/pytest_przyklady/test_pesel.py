"""
Przykłady testów dla modułu generującego uproszczony numer PESEL.

Plik pokazuje trzy podstawowe style pracy z pytest:
- prosty test z jednym `assert`,
- parametryzację,
- fixture ze wspólnymi danymi testowymi.
"""

import pytest

from moj_pakiet.pytest_przyklady.do_testow_pesel import rob_pesel


# Te same dane są użyte w parametryzacji i w fixture.
DANE_TESTOWE = [
    ((1987, 10, 9, 530, True), "87100953014"),
    ((1971, 9, 16, 459, True), "71091645913"),
    ((1986, 6, 4, 17, True), "86060401713"),
    ((1966, 11, 9, 344, True), "66110934415"),
    ((1963, 5, 17, 642, True), "63051764215"),
    ((2008, 10, 18, 733, True), "08301873314"),
    ((1967, 2, 13, 62, True), "67021306218"),
    ((1965, 2, 23, 551, True), "65022355110"),
    ((1968, 6, 21, 274, True), "68062127417"),
    ((1990, 4, 19, 386, True), "90041938611"),
    ((1995, 3, 25, 441, True), "95032544114"),
    ((1979, 7, 21, 356, True), "79072135611"),
    ((2005, 2, 13, 820, True), "05221382014"),
    ((1993, 11, 12, 755, True), "93111275515"),
    ((2006, 5, 16, 255, True), "06251625513"),
    ((1988, 2, 13, 824, True), "88021382417"),
    ((1981, 9, 18, 134, True), "81091813416"),
    ((1967, 2, 13, 515, True), "67021351511"),
    ((1971, 1, 25, 324, True), "71012532416"),
    ((2011, 1, 8, 889, True), "11210888919"),
]


@pytest.fixture(scope="module")
def dane_pesel():
    """Fixture zwracająca wspólny zestaw danych dla kilku testów."""
    yield DANE_TESTOWE


def test_rob_pesel_dla_pojedynczego_przypadku():
    """Najprostszy test: jeden przypadek i jedno oczekiwanie."""
    assert rob_pesel(2002, 11, 3, 34, True) == "02310303417"


def test_rob_pesel_dla_kobiety():
    """Drugi prosty test pokazujący inny wariant danych wejściowych."""
    assert rob_pesel(1990, 5, 12, 67, False) == "90051206700"


@pytest.mark.parametrize(("dane_wejsciowe", "oczekiwany_pesel"), DANE_TESTOWE)
def test_rob_pesel_parametryzacja(dane_wejsciowe, oczekiwany_pesel):
    """Ten sam test uruchomiony wielokrotnie dla wielu danych."""
    assert rob_pesel(*dane_wejsciowe) == oczekiwany_pesel


def test_rob_pesel_z_fixtura(dane_pesel):
    """Fixture pozwala współdzielić przygotowane dane między testami."""
    for dane_wejsciowe, oczekiwany_pesel in dane_pesel:
        assert rob_pesel(*dane_wejsciowe) == oczekiwany_pesel
