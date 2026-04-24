"""
Przykład testów korzystających z fixture ładującej dane z pliku JSON.

Plik pokazuje jeden wspólny fixture modułowy i dwa testy:
- test poprawnych wywołań,
- test przypadków błędnych.
"""

import json
from pathlib import Path
import pytest
from moj_pakiet.pytest_przyklady.do_testow_pesel import rob_pesel


SCIEZKA_DANYCH = Path(__file__).with_name("dane_pesel_fixture.json")
WYJATKI = {
    "TypeError": TypeError,
    "ValueError": ValueError,
}

@pytest.fixture(scope="session", autouse=True)
def dane_pesel_z_json():
    # print('\n fixture dane_pesel_z_json\n')
    """Ładuje dane testowe z pliku JSON raz na cały moduł."""
    with SCIEZKA_DANYCH.open(encoding="utf8") as plik:
        return json.load(plik)

@pytest.fixture(scope='session')
def srodowisko():
    # print('\n przygotowuję środowisko\n')
    yield 22
    # print('\n czyszczę środowisko\n')


@pytest.fixture(scope="module")
def poprawne_przypadki_pesel(dane_pesel_z_json):
    """Wydziela z pełnego JSON-a tylko przypadki poprawnych wywołań."""
    return dane_pesel_z_json["poprawne"]


@pytest.fixture(scope="module")
def bledne_przypadki_pesel(dane_pesel_z_json):
    """Wydziela z pełnego JSON-a tylko przypadki błędnych wywołań."""
    return dane_pesel_z_json["bledy"]


def test_rob_pesel_poprawne_wartosci_z_fixture(poprawne_przypadki_pesel):
    """Sprawdza poprawne przypadki przekazane już przez pośredni fixture."""
    for przypadek in poprawne_przypadki_pesel:
        assert rob_pesel(*przypadek["args"]) == przypadek["expected"]


def test_rob_pesel_bledy_z_fixture(bledne_przypadki_pesel):
    """Sprawdza błędy na podstawie danych przekazanych przez pośredni fixture."""
    for przypadek in bledne_przypadki_pesel:
        typ_wyjatku = WYJATKI[przypadek["exception"]]

        with pytest.raises(typ_wyjatku, match=przypadek["message"]):
            rob_pesel(*przypadek["args"])

def test_prosty_1(srodowisko):
    print('\n test_prosty_1 \n')

def test_prosty_2(srodowisko):
    print('\n test_prosty_2 \n')
