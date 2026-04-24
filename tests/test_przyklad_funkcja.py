import pytest
from moj_pakiet.przyklad_funkcja import dodaj_liczby, podziel_liczby

dane = [
        (2, 3, 5),
        (-4, 10, 6),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ]

@pytest.mark.parametrize(("a", "b", "expected"), dane)
def test_dodaj_liczby_zwraca_sume(a, b, expected):
    assert dodaj_liczby(a, b) == expected

dane1 = [
        ((2, 3), 5),
        ((-4, 10), 6),
        ((0, 0), 0),
        ((1.5, 2.5), 4.0),
    ]
#  uwaga - parametrize generuje type testcasów ile danych - potencjalnie bardzo dużo!!!
@pytest.mark.parametrize(("args", "expected"), dane1)
def test_dodaj_liczby_zwraca_sume_1(args, expected):
    assert dodaj_liczby(*args) == expected

def test1():
    assert dodaj_liczby(1, 2) == 3
    x = [1,2,3,4]
    assert 4 in x
    assert dodaj_liczby(.1, .2) == pytest.approx(.3)

def test_dzielenie():
    assert podziel_liczby(9, 3) == 3
    with pytest.raises(ZeroDivisionError):
        podziel_liczby(9, 0)
    with pytest.raises(ZeroDivisionError):
        podziel_liczby(3, 0)