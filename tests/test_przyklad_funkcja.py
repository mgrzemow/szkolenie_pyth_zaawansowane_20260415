import pytest

from moj_pakiet.przyklad_funkcja import dodaj_liczby


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-4, 10, 6),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_dodaj_liczby_zwraca_sume(a, b, expected):
    assert dodaj_liczby(a, b) == expected
