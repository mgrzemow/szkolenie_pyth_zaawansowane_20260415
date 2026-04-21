"""
Przykłady testów osiągających ten sam efekt co dawniej z `monkeypatch`,
ale z użyciem fixture `mocker` z pluginu `pytest-mock`.

Tutaj zależność `requests.get` jest podmieniana przez `mocker.patch.object`,
a `mocker.MagicMock()` pozwala dodatkowo sprawdzać liczbę wywołań i argumenty.
"""

from moj_pakiet.pytest_przyklady import do_testow_http


def test_pobierz_json_z_magicmock(mocker):
    """`mocker.MagicMock()` może udawać odpowiedź HTTP tak samo jak ręczny fake."""
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = {"id": 11, "nazwa": "demo"}

    mock_get = mocker.patch.object(
        do_testow_http.requests,
        "get",
        return_value=mock_response,
    )
    wynik = do_testow_http.pobierz_json("https://example.invalid/api")

    assert wynik["id"] == 11
    assert wynik["nazwa"] == "demo"

    # Mock pamięta sposób wywołania, więc łatwo sprawdzić argumenty.
    mock_get.assert_called_once_with("https://example.invalid/api", timeout=5)
    mock_response.json.assert_called_once_with()


def test_pobierz_wartosc_i_zliczaj_wywolania_magicmock(mocker):
    """MagicMock pozwala liczyć wywołania i sprawdzać historię użycia zależności."""
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = {"liczba": 22}

    mock_get = mocker.patch.object(
        do_testow_http.requests,
        "get",
        return_value=mock_response,
    )

    wynik_1 = do_testow_http.pobierz_wartosc(
        "https://example.invalid/liczba",
        "liczba",
    )
    wynik_2 = do_testow_http.pobierz_wartosc(
        "https://example.invalid/liczba",
        "liczba",
    )

    assert wynik_1 == 22
    assert wynik_2 == 22

    # Ten sam mock był użyty dwa razy, więc można odczytać licznik wywołań.
    assert mock_get.call_count == 2
    assert mock_response.json.call_count == 2

    # `call_args_list` przechowuje pełną historię wywołań w kolejności.
    assert mock_get.call_args_list[0].args == ("https://example.invalid/liczba",)
    assert mock_get.call_args_list[0].kwargs == {"timeout": 5}
    assert mock_get.call_args_list[1].args == ("https://example.invalid/liczba",)
    assert mock_get.call_args_list[1].kwargs == {"timeout": 5}
