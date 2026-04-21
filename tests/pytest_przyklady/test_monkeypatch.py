"""
Przykłady testów wykorzystujących plugin `pytest-mock`.

Fixture `mocker` upraszcza patchowanie zależności i automatycznie sprząta
po teście, więc nie trzeba ręcznie zarządzać obiektem `patch`.
"""

from moj_pakiet.pytest_przyklady import do_testow_http


def test_pobierz_json_z_mocker(mocker):
    """`mocker.patch.object` podmienia zależność podobnie jak monkeypatch."""

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
    mock_get.assert_called_once_with("https://example.invalid/api", timeout=5)
    mock_response.json.assert_called_once_with()


def test_pobierz_wartosc_z_mocker(mocker):
    """Drugi test pokazuje ten sam mechanizm dla innego wariantu odpowiedzi."""

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = {"status": "ok", "liczba": 22}

    mock_get = mocker.patch.object(
        do_testow_http.requests,
        "get",
        return_value=mock_response,
    )

    wynik = do_testow_http.pobierz_wartosc("https://example.invalid/liczba", "liczba")
    assert wynik == 22
    mock_get.assert_called_once_with("https://example.invalid/liczba", timeout=5)
    mock_response.json.assert_called_once_with()
